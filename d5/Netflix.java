import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.conf.Configuration;

import java.io.*;

public class Netflix {
	public static class NetflixMapper extends Mapper<LongWritable, Text, Text, FloatWritable>{
		public void map(LongWritable key, Text value, Context context)
			throws IOException, InterruptedException{
			String line = value.toString();
			if(line.startsWith("userId")) return;
			String[] fields = line.split(",");
			String movieId = fields[1];
			FloatWritable rating = new FloatWritable(Float.parseFloat(fields[2]));
			context.write(new Text(movieId), rating);
		}
	}
	
	public static class NetflixReducer extends Reducer<Text, FloatWritable, Text, FloatWritable>{
		public void reduce(Text key, Iterable<FloatWritable> values, Context context)
			throws IOException, InterruptedException{
			float sum = 0;
			int count = 0;
			for(FloatWritable value: values){
				sum+=value.get();
				count++;
			}
			float average = sum/count;
			context.write(key, new FloatWritable(average));
		}
	}
	
	public static void main(String[] args) throws Exception{
		Configuration conf = new Configuration();
		Job job = Job.getInstance(conf, "movie analysis");
    
		job.setJarByClass(Netflix.class);
		job.setMapperClass(NetflixMapper.class);
		job.setReducerClass(NetflixReducer.class);
		
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(FloatWritable.class);
		
		FileInputFormat.addInputPath(job, new Path(args[0]));
		FileOutputFormat.setOutputPath(job, new Path(args[1]));
		System.exit(job.waitForCompletion(true)?0:1);
	}
}

import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;

import java.io.*;

import org.apache.hadoop.conf.Configuration;
public class MusicAlanysis {
	public static class MusicMapper extends Mapper<LongWritable, Text, Text, Text>{
		
		public void map(LongWritable key, Text value, Context context)
		throws IOException, InterruptedException
		{
			String line = value.toString();
			if(line.startsWith("UserId")){
				return;
			}
			String[] fields = line.split(",");
			String trackId = fields[1];
			String onRadio = fields[3].trim();
			String skipped = fields[4].trim();
			
			context.write(new Text(trackId), new Text(onRadio+","+skipped));
		}
	}
	
	public static class MusicReducer extends Reducer<Text, Text, Text, Text>{
		int totalOnRadio = 0;
		int totalSkipped = 0;
		public void reduce(Text key, Iterable<Text> values, Context context)
		throws IOException, InterruptedException
		{
			for(Text value: values){
				String[] params = value.toString().split(",");
				int onRadio = new Integer(params[0]);
				int skipped = new Integer(params[1]);
				totalOnRadio+=onRadio;
				totalSkipped+=skipped;
			}
			context.write(key, new Text(totalOnRadio+", "+totalSkipped));
			totalOnRadio = 0;
			totalSkipped = 0;
		}
	}
	
	public static void main(String[] args) throws Exception{
		Configuration conf = new Configuration();
		Job job = Job.getInstance(conf, "music alanysis");
		
		job.setJarByClass(MusicAlanysis.class);
		job.setMapperClass(MusicMapper.class);
		job.setReducerClass(MusicReducer.class);
		
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(Text.class);
		
		FileInputFormat.addInputPath(job, new Path(args[0]));
		FileOutputFormat.setOutputPath(job, new Path(args[1]));
		System.exit(job.waitForCompletion(true) ? 0 : 1);
		
	}
}

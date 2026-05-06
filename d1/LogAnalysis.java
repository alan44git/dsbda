import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class LogAnalysis {

    public static class LogMapper extends Mapper<LongWritable, Text, Text, LongWritable> {

        private SimpleDateFormat sdf = new SimpleDateFormat("dd-MM-yyyy HH:mm");

        public void map(LongWritable key, Text value, Context context)
                throws IOException, InterruptedException {

            try {
                String[] fields = value.toString().split("\\t");

                String mac = fields[0];
                String loginTime = fields[5];
                String logoutTime = fields[7];

                Date login = sdf.parse(loginTime);
                Date logout = sdf.parse(logoutTime);

                long duration = (logout.getTime() - login.getTime()) / (1000 * 60); // minutes

                context.write(new Text(mac), new LongWritable(duration));

            } catch (Exception e) {
                // Ignore bad records
            }
        }
    }

    public static class LogReducer extends Reducer<Text, LongWritable, Text, LongWritable> {

        public void reduce(Text key, Iterable<LongWritable> values, Context context)
                throws IOException, InterruptedException {

            long total = 0;

            for (LongWritable val : values) {
                total += val.get();
            }

            context.write(key, new LongWritable(total));
        }
    }

    public static void main(String[] args) throws Exception {

        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "Log Analysis");

        job.setJarByClass(LogAnalysis.class);

        job.setMapperClass(LogMapper.class);
        job.setReducerClass(LogReducer.class);

        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(LongWritable.class);

        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
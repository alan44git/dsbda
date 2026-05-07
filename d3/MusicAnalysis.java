import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;

import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;

import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class TrackStats {

    // Mapper Class
    public static class StatsMapper
            extends Mapper<LongWritable, Text, Text, IntWritable> {

        private final static IntWritable one = new IntWritable(1);
        private Text outKey = new Text();

        public void map(LongWritable key, Text value, Context context)
                throws IOException, InterruptedException {

            String line = value.toString();

            // Skip header
            if (line.startsWith("UserId")) {
                return;
            }

            String[] fields = line.split(",");

            // Dataset format:
            // UserId,TrackId,Shared,Radio,Skip

            String userId = fields[0];
            String trackId = fields[1];
            String shared = fields[2];

            // Emit user for unique listener count
            outKey.set("USER_" + userId);
            context.write(outKey, one);

            // Emit track if shared
            if (shared.equals("1")) {
                outKey.set("TRACK_" + trackId);
                context.write(outKey, one);
            }
        }
    }

    // Reducer Class
    public static class StatsReducer
            extends Reducer<Text, IntWritable, Text, IntWritable> {

        int uniqueUsers = 0;

        public void reduce(Text key, Iterable<IntWritable> values,
                           Context context)
                throws IOException, InterruptedException {

            String currentKey = key.toString();

            // Count unique users
            if (currentKey.startsWith("USER_")) {

                uniqueUsers++;

            }
            // Count shares per track
            else if (currentKey.startsWith("TRACK_")) {

                int sum = 0;

                for (IntWritable val : values) {
                    sum += val.get();
                }

                String trackId = currentKey.replace("TRACK_", "");

                context.write(
                        new Text("Track " + trackId + " shared"),
                        new IntWritable(sum)
                );
            }
        }

        @Override
        protected void cleanup(Context context)
                throws IOException, InterruptedException {

            context.write(
                    new Text("Total unique listeners"),
                    new IntWritable(uniqueUsers)
            );
        }
    }

    // Driver Class
    public static void main(String[] args) throws Exception {

        Configuration conf = new Configuration();

        Job job = Job.getInstance(conf, "Track Statistics");

        job.setJarByClass(TrackStats.class);

        job.setMapperClass(StatsMapper.class);
        job.setReducerClass(StatsReducer.class);

        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
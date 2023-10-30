from pyspark import SparkContext, SparkConf

def main():
    # Initialize Spark
    conf = SparkConf().setAppName("HelloWorldApp")
    sc = SparkContext(conf=conf)

    # Create an RDD
    words = ["Hello", "World", "This", "is", "a", "Spark", "app"]
    words_rdd = sc.parallelize(words)

    # Transform the RDD
    word_lengths = words_rdd.map(lambda word: (word, len(word)))

    # Action to collect results
    output = word_lengths.collect()

    # Print results
    for (word, length) in output:
        print(f"{word} : {length}")

    # Stop the SparkContext
    sc.stop()

if __name__ == "__main__":
    main()

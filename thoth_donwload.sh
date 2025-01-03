dir='/Volumes/SSD/LLM-Model/thoth/'
model='hdfs://harunava/home/byte_tteng_llm_release/model/long-thoth-1b2-v3'
/Volumes/SSD/LLM-Model/hadoop-3.4.0/bin/hdfs dfs -get "$model" "$dir"
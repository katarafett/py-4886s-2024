OUTPUT_FILE="./tmp.tmp"
READ_FILE="./all-files.txt"
IMPORTS="./include/imports.py"

# Create and clear a temporary file
echo "" > $OUTPUT_FILE

# Add specified files
while read line;
do
    INPUT_FILE=$line
    # Add a header before each file
    echo "\n\n\n# $INPUT_FILE ---" >> $OUTPUT_FILE

    cat $INPUT_FILE >> $OUTPUT_FILE
done < $READ_FILE

# Delete import lines
sed -i.bak "/^from /d" $OUTPUT_FILE
sed -i.bak "/^import /d" $OUTPUT_FILE
rm ${OUTPUT_FILE}.bak

INPUT_FILE=$OUTPUT_FILE
OUTPUT_FILE="./main.py"
# Add stdlib imports
cat $IMPORTS > $OUTPUT_FILE

# Add the rest of the file
cat $INPUT_FILE >> $OUTPUT_FILE

# Remove in-between file
rm $INPUT_FILE

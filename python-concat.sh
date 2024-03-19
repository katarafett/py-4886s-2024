# Create file
OUTPUT_FILE="./tmp.tmp"

INPUT_FILE="./src/stddefs.py"
echo "\n\n\n# $INPUT_FILE ---" > $OUTPUT_FILE
cat $INPUT_FILE >> $OUTPUT_FILE

INPUT_FILE="./src/robot_config.py"
echo "\n\n\n# $INPUT_FILE ---" >> $OUTPUT_FILE
cat $INPUT_FILE >> $OUTPUT_FILE

INPUT_FILE="./src/util.py"
echo "\n\n\n# $INPUT_FILE ---" >> $OUTPUT_FILE
cat $INPUT_FILE >> $OUTPUT_FILE

INPUT_FILE="./src/pid.py"
echo "\n\n\n# $INPUT_FILE ---" >> $OUTPUT_FILE
cat $INPUT_FILE >> $OUTPUT_FILE

INPUT_FILE="./src/movement.py"
echo "\n\n\n# $INPUT_FILE ---" >> $OUTPUT_FILE
cat $INPUT_FILE >> $OUTPUT_FILE

INPUT_FILE="./src/tune_pid.py"
echo "\n\n\n# $INPUT_FILE ---" >> $OUTPUT_FILE
cat $INPUT_FILE >> $OUTPUT_FILE

INPUT_FILE="./src/preauton.py"
echo "\n\n\n# $INPUT_FILE ---" >> $OUTPUT_FILE
cat $INPUT_FILE >> $OUTPUT_FILE

INPUT_FILE="./src/auton.py"
echo "\n\n\n# $INPUT_FILE ---" >> $OUTPUT_FILE
cat $INPUT_FILE >> $OUTPUT_FILE

INPUT_FILE="./src/opcontrol.py"
echo "\n\n\n# $INPUT_FILE ---" >> $OUTPUT_FILE
cat $INPUT_FILE >> $OUTPUT_FILE

INPUT_FILE="./src/main.py"
echo "\n\n\n# $INPUT_FILE ---" >> $OUTPUT_FILE
cat $INPUT_FILE >> $OUTPUT_FILE

# Delete import lines
gsed -i "/^from /d" $OUTPUT_FILE
gsed -i "/^import /d" $OUTPUT_FILE

INPUT_FILE=$OUTPUT_FILE
OUTPUT_FILE="./main.py"
# Add stdlib imports
echo "import vex
import math" > $OUTPUT_FILE

# Add the rest of the file
cat $INPUT_FILE >> $OUTPUT_FILE

# Remove in-between file
rm $INPUT_FILE

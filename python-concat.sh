OUTPUT_FILE="./test.txt"

INPUT_FILE="./src/stddefs.py"
echo "\n# $INPUT_FILE ---" > $OUTPUT_FILE
cat $INPUT_FILE >> $OUTPUT_FILE

INPUT_FILE="./src/robot_config.py"
echo "\n# $INPUT_FILE ---" >> $OUTPUT_FILE
cat $INPUT_FILE >> $OUTPUT_FILE

INPUT_FILE="./src/util.py"
echo "\n# $INPUT_FILE ---" >> $OUTPUT_FILE
cat $INPUT_FILE >> $OUTPUT_FILE

INPUT_FILE="./src/pid.py"
echo "\n# $INPUT_FILE ---" >> $OUTPUT_FILE
cat $INPUT_FILE >> $OUTPUT_FILE

INPUT_FILE="./src/movement.py"
echo "\n# $INPUT_FILE ---" >> $OUTPUT_FILE
cat $INPUT_FILE >> $OUTPUT_FILE

INPUT_FILE="./src/tune_pid.py"
echo "\n# $INPUT_FILE ---" >> $OUTPUT_FILE
cat $INPUT_FILE >> $OUTPUT_FILE

INPUT_FILE="./src/preauton.py"
echo "\n# $INPUT_FILE ---" >> $OUTPUT_FILE
cat $INPUT_FILE >> $OUTPUT_FILE

INPUT_FILE="./src/auton.py"
echo "\n# $INPUT_FILE ---" >> $OUTPUT_FILE
cat $INPUT_FILE >> $OUTPUT_FILE

INPUT_FILE="./src/opcontrol.py"
echo "\n# $INPUT_FILE ---" >> $OUTPUT_FILE
cat $INPUT_FILE >> $OUTPUT_FILE

INPUT_FILE="./src/main.py"
echo "\n# $INPUT_FILE ---" >> $OUTPUT_FILE
cat $INPUT_FILE >> $OUTPUT_FILE

# beep_test_video
Convert a video to beep test info with levels and team name


## Convert a video to a beep test 

## Example of usage 

this commmand will convert video input.mov into a new video output.mp4 it will watermark with team name TEAM_NAME and will start the beep test at 01 seconds.  

```
beep.py -s 1 -t YOUR_TEAM_NAME -v input.mov -o output.mp4 | sh 
```

help message 

```
beep.py --help
usage: beep.py [-h] [-s START_TIME] [-t TEAM] [-v VIDEO] [-o OUTPUT]

options:
  -h, --help            show this help message and exit
  -s START_TIME, --start-time START_TIME
                        time in the video when actual beep test starts, use if your video has 2-3 seconds of time prior to first beep
  -t TEAM, --team TEAM  PORT to bind on
  -v VIDEO, --video VIDEO
                        input video, path to file
  -o OUTPUT, --output-video OUTPUT
                        output video
```

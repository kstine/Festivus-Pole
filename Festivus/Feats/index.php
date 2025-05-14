<?php 
/***
Reindeer php web interface
see http://www.penguintutor.com/electronics/reindeer

There is no security in this including any attempt at authentication
- this is intended for a novelty display only

***/


$playnowfile = '/home/pi/reindeer/playnow.cfg';
$settingsfile = '/home/pi/reindeer/reindeer.cfg';

# Text for status message - ie did we update
$status = '';

if (isset($_POST['do']) && $_POST['do']=='play')
{
	# touch the file - updates mtime to prompt to play
	touch ($playnowfile);
	$status = "Playing";
}
elseif (isset($_POST['savesettings']) && $_POST['savesettings']=='yes')
{
	# Get settings - if any settings missing / not valid then use defaults
	# We just compare against settings that are allowed for security reasons
	
	# Get sound setting
	if (isset($_POST['sound']) && $_POST['sound'] == 'off')
	{
		$newsetting_sound = 'off';
	}
	else
	{
		$newsetting_sound = 'on';
	}
	
	# Get mode setting
	if (isset($_POST['mode']) && $_POST['mode'] == 'off')
	{
		$newsetting_mode = 'off';
	}
	elseif (isset($_POST['mode']) && $_POST['mode'] == 'on') 
	{
		$newsetting_mode = 'on';
	}
	else
	{
		$newsetting_mode = 'pir';
	}
	
	#Write settings to file 
	$fh = fopen($settingsfile, 'w');
	fputs ($fh,  "##Settings for Raspberry Pi Reindeer\n#See http://www.penguintutor.com/electronics/reindeer/\n");
	fputs ($fh, 'sound='.$newsetting_sound."\n");
	fputs ($fh, 'mode='.$newsetting_mode."\n");
	
	
}




##Display standard web page regardless of whether update
# Uses $status field to report back any update


# default values 
$setting_sound = '';
$setting_mode = '';


# Load current settings for default form values
$fr = fopen($settingsfile, 'r');
if ($fr)
{
	while (($buffer = fgets($fr, 4096)) !== false)
	{
		# Ignore any entries other than sound and mode
		# As the file should be system generated we know entire line so just perform string compare
		$buffer = trim($buffer);
		if (strcmp ("sound=on", $buffer) == 0) {$setting_sound = 'on';}
		elseif (strcmp ("sound=off", $buffer) == 0) {$setting_sound = 'off';}
		elseif (strcmp ("mode=pir", $buffer) == 0) {$setting_mode = 'pir';}
		elseif (strcmp ("mode=on", $buffer) == 0) {$setting_mode = 'on';}
		elseif (strcmp ("mode=off", $buffer) == 0) {$setting_mode = 'off';}
	}
	fclose($fr);
}


# create setting entries using current values
# Sound	
$html_sound = "Sound: ";
if ($setting_sound == 'on') {$html_sound.='<input type="radio" name="sound" value="on" checked="checked"> on ';}
else {$html_sound.='<input type="radio" name="sound" value="on"> on ';}
if ($setting_sound == 'off') {$html_sound.='<input type="radio" name="sound" value="off" checked="checked"> off ';}
else {$html_sound.='<input type="radio" name="sound" value="off"> off ';}
$html_sound.=" <br>";

# Mode
$html_mode = "Mode: ";
if ($setting_mode == 'pir') {$html_mode.='<input type="radio" name="mode" value="pir" checked="checked"> PIR ';}
else {$html_mode.='<input type="radio" name="mode" value="pir"> PIR ';}
if ($setting_mode == 'on') {$html_mode.='<input type="radio" name="mode" value="on" checked="checked"> on ';}
else {$html_mode.='<input type="radio" name="mode" value="on"> on ';}
if ($setting_mode == 'off') {$html_mode.='<input type="radio" name="mode" value="off" checked="checked"> off ';}
else {$html_mode.='<input type="radio" name="mode" value="off"> off ';}
$html_mode.="<br>";
	

print <<<EOT

<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Raspberry Pi - Reindeer</title>

<script src=""></script>


<link href="reindeer.css" rel="stylesheet" type="text/css">
</head>
<body>
<h1>Talking reindeer</h1>
<h2>Powered by Raspberry Pi</h2>

<div id="intro">
<p><img id="reindeerimg" class="mainimg" src="reindeer.jpg" alt="Raspberry Pi powered Christmas Reindeer"></p>
</div>

<div id="playnow">

<form id="playnowform" action="index.php" method="post">
<input type="hidden" name="do" value="play">
<!-- <input type="submit" value="Play now" />  -->
</form>

<p>Click on the reindeer to play now.</p>

</div>

<div id="settings">
<h2>Settings</h2>

<form id="settingsform" action="index.php" method="post">
<input type="hidden" name="savesettings" value="yes">
$html_sound
$html_mode
<input type="submit" value="Save">
</form>



</div>





<div id="about"><p>See <a href="http://www.penguintutor.com/electronics/reindeer">PenguinTutor Raspberry Pi Reindeer project</a></p></div>

<script src="reindeer.js"></script>

</body>
</html>
EOT;





# Custom Capes
*This is a very basic, version 1 prototype. Gonna be adding more stuff later.* 
<details>
  <summary><strong>Table of contents</strong></summary>

- [Installation](#installation)
- [Capes](#capes)
- [How it works](#how-it-works)
- [Contact](#contact)

</details>
<br><br> 

**Credit**<br>
I found the default minecraft capes all over the place, but most come from: `https://github.com/ewanhowell5195/customOptiFineCapeServer/tree/main/capes/default`

# Installation


**Must be using a version of Minecraft with Optifine on Windows**<br><br>
Download or Clone Repository<br><br>
In the /capes folder, rename a cape to (Your Minecraft Username).png<br>

   ![imgur](https://imgur.com/pZTXexf.png)

<br>After Minecraft has loaded to the home screen, run ccapes.py or ccapes.exe
<br>

<br>*Must be run as administrator, as it modifies files in sys32*

<br>

# Capes

Capes must be stored in the /capes folder
<br>
Any custom capes must use the elytra texture
<br>
Anytime you change the cape while the program is running: `Settings -> Skin Customization -> Optifine Cape -> Reload Cape`

# How It Works


Optifine makes requests to `s.optifine.net` with the Username of the account that it's trying to load the cape from.
<br>
For example: `s.optifine.net/capes/notch.png`, would return the png of the cape for that account
<br>
We modify the hosts file, which redirects `s.optifine.net -> 127.0.0.1`
<br>When Optifine tries to load the cape, our local server responds instead: `127.0.0.1:80/capes/notch.png` with the custom cape for that filename

# Contact
If you have any suggestions, issues or questions, send me a message on discord: `chromiumsucks#0001`


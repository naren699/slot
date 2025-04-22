<<<<<<< HEAD
# Ex-03 Time Table
=======
# Ex03 Time Table
>>>>>>> 1570281 (Success)
## Date: 22-04-2025

## AIM
To write a html webpage page to display your slot timetable.

## ALGORITHM
### STEP 1
Create a Django-admin Interface.

### STEP 2
Create a static folder and inert HTML code.

### STEP 3
<<<<<<< HEAD
Create a simple table using ```<table>``` tag in html.

### STEP 4
Add header row using ```<th>``` tag.

### STEP 5
Add your timetable using ```<td>``` tag.
=======
Create a simple table using <table> tag in html.

### STEP 4
Add header row using <th> tag.

### STEP 5
Add your timetable using <td> tag.
>>>>>>> 1570281 (Success)

### STEP 6
Execute the program using runserver command.

## PROGRAM
<<<<<<< HEAD

``` html
<html>
<head>
<title> Course Schedule </title>
</head>
<body>
<br>
<table align="center" width="540" cellspacing="2" cellpadding="4" border="5" bgcolor="cyan">
<caption><b>SCHEDULE OF ALL COURSES - LAKSHMIDHAR N (212224230138)</b></caption>
<tr align="center">
<th bgcolor="yellow">Day/Time</th>
<th bgcolor="yellow">Monday</th>
<th bgcolor="yellow">Tuesday</th>
<th bgcolor="yellow">Wednesday</th>
<th bgcolor="yellow">Thursday</th>
<th bgcolor="yellow">Friday</th>
</tr>
<tr align="center">
<th bgcolor="yellow">8-10</th>
<td >FREE SLOT</td>
<td>FREE SLOT</td>
<td>FREE SLOT</td>
<td>C PROGRAMMING</td>
<td>C PROGRAMMING</td>
</tr>
<tr align="center">
<th bgcolor="yellow">10-12</th>
<td>BEEE</td>
<td> OPERATING SYSTEMS</td>
<td>OPERATING SYSTEMS</td>
<td>STATISTICS</td>
<td>FUNDAMENTALS OF WEB</td>
</tr>
<tr>
<th bgcolor="yellow">12-1</th>
<td colspan="5" align="center">L U N C H</td>
</tr>
<tr align="center">
<th bgcolor="yellow">1-3</th>
<td >STATISTICS</td>
<td>DBMS</td>
<td>MENTOR MEET</td>
<td>PHYSICS</td>
<td>PHYSICS</td>
</tr>
<tr align="center">
<th bgcolor="yellow">3-5</th>
<td>FREE SLOT</td>
<td>FREE SLOT</td>
<td>FUNDAMENTALS OF WEB</td>
<td>REASONING ABILITY</td>
<td>BEEE</td>
</tr>
</table>
<br>
<table align="center" cellspacing="2" cellpadding="4" border="2">
<tr align="center">
<th>S. No.</th>
<th>Subject Code</th>
<th>Subject Name</th>
</tr>
<tr>
<td align="center">1.</td>
<td align="center">19AI414</td>
<td>FUNDAMENTALS OF WEB APPLICATION DEVELOPMENT (FWAD)</td>
</tr>
<tr>
<td align="center">2.</td>
<td align="center">19AI304</td>
<td>FUNDAMENTALS OF C PROGRAMMING (C PROGRAM)</td>
</tr>
<tr>
<td align="center">3.</td>
<td align="center">19PH814</td>
<td> PHYSICS FOR QUANTUM COMPUTING (PHY)</td>
</tr>
<tr>
<td align="center">4.</td>
<td align="center">19CS405</td>
<td>OPERATING SYSTEMS (OS)</td>
</tr>
<tr>
<td align="center">5.</td>
<td align="center">19MA211</td>
<td>STATISTICS AND NUMERICAL METHODS (MAT)</td>
</tr>
<tr>
<td align="center">6.</td>
<td align="center">19CS404</td>
<td>DATABASE MANAGEMENT SYSTEMS AND ITS APPLICATIONS (DBMS)</td>
</tr>
<td align="center">7.</td>
<td align="center">19EY709</td>
<td>REASONING ABILITY (RA)</td>
</tr>
<td align="center">8.</td>
<td align="center">19EE305</td>
<td>BASIC ELECTRICAL ELECTRONICS AND MEASUREMENT ENGINEERING (BEEE)</td>
</table>
</body>
</html>
```

## OUTPUT
![OUTPUT](./Screenshot%202025-04-22%20081415.png)

## RESULT
The program for creating slot timetable using basic HTML tags is executed successfully.
=======
```
<html>
    <body>
        <img src="logo.png" height="100" width="560"> 
        <table border="1" cellspacing="2" cellpadding="2">
            <caption>SLOT TIME TABLE NARENDHIRAN.P(212224230177)</caption>
            <tr bgcolor="red">
                <th>Day/time</th>
                <th>monday</th>
                <th>tuesday</th>
                <th>wednesday</th>
                <th>thursday</th>
                <th>friday</th>
                <th>saturday</th>
            </tr>
            <tr>
                <td bgcolor="yellow">8-10</td>
                <td bgcolor="cyan" colspan="4">FREE SLOT</td>
                <td bgcolor="cyan">C PROGROM</td>
                <td bgcolor="cyan">FREE SLOT</td>
            </tr>
            <tr>
                <td bgcolor="yellow">10-12</td>
                <td bgcolor="cyan">OS</td>
                <td bgcolor="cyan">WEB</td>
                <td bgcolor="cyan">MATHS</td>
                <td bgcolor="cyan">FREE SLOT</td>
                <td bgcolor="cyan">C PROGRAM</td>
                <td bgcolor="cyan">FREE SLOT</td>
            </tr>
            <tr>
                <td bgcolor="yellow">12-1</td>
                <td bgcolor="cyan" colspan="6" align="center">LUNCH</td>
            </tr>
            <tr>
                <td bgcolor="yellow">1-3</td>
                <td bgcolor="cyan">MATHS</td>
                <td bgcolor="cyan">C PROGRAM</td>
                <td bgcolor="cyan">MENTOR</td>
                <td bgcolor="cyan">PQM</td>
                <td bgcolor="cyan">MATHS</td>
                <td bgcolor="cyan">WEB</td>
            </tr>
            <tr>
                <td bgcolor="yellow">3-5</td> 
                <td bgcolor="cyan">EDM</td>
                <td bgcolor="cyan" colspan="4">FREE SLOT</td>
                <td bgcolor="cyan">EDM</td>
            </tr>
        </table>
        <br>
        <table  border="1" cellpadding="2">
            <tr>
                <td>s.no</td>
                <td>course code</td>
                <td align="center">Course Name</td>
            </tr>
            <tr>
                <td>1</td>
                <td>19AI414</td>
                <td>Fundamental of web application development </td>
            </tr>
            <tr>
                <td>2</td>
                <td>19AI304</td>
                <td>Fundamental of C programming</td>
            </tr>
            <tr>
                <td>3</td>
                <td>19MA220</td>
                <td>Mathematics for AI</td>
            </tr>
            <tr>
            <td>4</td>
            <td>19AI303</td>
            <td>Engineeing Mechanics and Product</td>
            </tr>
            <tr>
                <td>5</td>
                <td>19AI410</td>
                <td>Intorduction to ML</td>
            </tr>
            <tr>
                <td>6</td>
                <td>19MA222</td>
                <td>Probability and Queueing Models</td>
            </tr>
            <tr>
            <td>7</td>
            <td>ECA-M SCOFT</td>
            <td>Mentor Meet</td>
            </tr>
            
             
        </table>
    </body>
 </html>
```

## OUTPUT

![alt text](<Screenshot 2025-04-22 204533.png>)

## RESULT
The program for creating slot timetable using basic HTML tags is executed successfully.
>>>>>>> 1570281 (Success)

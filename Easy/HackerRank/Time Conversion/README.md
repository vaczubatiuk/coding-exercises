# Time Conversion
Note: 
- `12:00:00AM` on a 12-hour clock is `00:00:00` on a 24-hour clock.
- `12:00:00PM` on a 12-hour clock is `12:00:00` on a 24-hour clock.

Example
```yaml
timeString = '12:01:00PM'
Return 
    '12:01:00'
timeString = '12:01:00AM'
    '12:01:00AM'
Return 
    '00:01:00'
timeString = '07:04:28PM'
Return 
    '19:04:28'
```
### Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

#### timeConversion has the following parameter(s):

&emsp;`string s: a time in 12-hour format`

#### Returns

&emsp;`string: the time in 24-hour format`

#### Input Format

&emsp;A single string  that represents a time in 12-hour clock format (i.e.: `hh:mm:ssAM` or `hh:mm:ssPM`).

### Constraints

&emsp;All input times are valid

#### Sample Input

&emsp;`07:05:45PM`

#### Sample Output

&emsp;`19:05:45`
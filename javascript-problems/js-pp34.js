// https://leetcode.com/problems/reformat-date/
// 1507. Reformat Date

/**
 * @param {string} date
 * @return {string}
 */
var reformatDate = function(date) {
    let month = { "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12" };
    let day = { "1st": "01", "2nd": "02", "3rd": "03", "4th": "04", "5th": "05", "6th": "06", "7th": "07", "8th": "08", "9th": "09", "10th": "10", "11th": "11", "12th": "12", "13th": "13", "14th": "14", "15th": "15", "16th": "16", "17th": "17", "18th": "18", "19th": "19", "20th": "20", "21st": "21", "22nd": "22", "23rd": "23", "24th": "24", "25th": "25", "26th": "26", "27th": "27", "28th": "28", "29th": "29", "30th": "30", "31st": "31" }

    date = date.split(" ")
    let result = ""
    for (let i = date.length - 1; i >= 0; i--) {
        if (i == date.length - 1) result += date[i] + "-"
        else if (i == 0) {
            result += day[date[i]]
        } else {
            if (date[i] in month) {
                result += month[date[i]] + "-"
            }
        }
    }
    return result
};
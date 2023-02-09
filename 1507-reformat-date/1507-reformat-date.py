class Solution:
    def reformatDate(self, date: str) -> str:
        months = {"Jan":'01', "Feb":'02', "Mar":'03', "Apr":'04', "May":'05', "Jun":'06', "Jul":'07', "Aug":'08', "Sep":'09', "Oct":'10', "Nov":'11', "Dec":'12'}
        date = date.split()[::-1]
        month = months[date[1]]
        date[1] = month
        date[-1] = date[-1][:-2].zfill(2)
        
        return '-'.join(date)
        
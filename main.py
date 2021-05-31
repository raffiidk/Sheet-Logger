import os
import gspread
import discord
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date
import time
scope = ['https://spreadsheets.google.com/feeds']
scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name("nexchange-bfdbbd41e03d.json",scope)
client = gspread.authorize(creds)
sheet = client.open("NexChange Logs").sheet1
datasheet = client.open("Nexchange data").sheet1
feesheet = client.open("Nexchange fees").sheet1

@client.event
async def on_message(message):
  if message.content.startswith('$list'):
      count = 290
      await channel.send("Finding row")
      count2 = count
      while True:
        count2 = count2 + 1
        cell = sheet.cell(count2,1).value
        if type(cell) == str and len(cell) > 1:     
          continue
        else:
          row = count2
          await channel.send("Available row: {}".format(count2))
          break
      user = message.author
      await channel.send('Log: Client,Client ID,Date,Price,Platform fees,Converter fees,Converter,Payment In,Payment Out, Transcript,Security Fee. Separate with comma.')
      msgstr = str(message.content)
      print(msgstr)
      while True:
        insert = row
        insert = int(insert)
        msg = await client.wait_for('message')
        if msg.author == message.author:
          content = msg.content
          string = str(content)
          split = string.split(",")
          log_data = split
          insertRow = log_data
          user = str(user)
          try:
            insertRow[3] = float(insertRow[3])
            print("row3")
            insertRow[4] = float(insertRow[4])
            #print("row4")
            insertRow[5] = float(insertRow[5])
            print("done int conv")
          except ValueError:
            await channel.send("Error converting to int, most likely data incomplete.")
            await channel.send('Log: Client,Client ID,Date,Price,Platform fees,Converter fees,Converter,Payment In,Payment Out, Transcript, Queue fee. Separate with comma.')
            continue
          if len(insertRow) < 11:
            await channel.send("Data incomplete, please fill out. Use 0 if data is not available (in the case of transcript etc.)")
            await channel.send('Log: Client,Client ID,Date,Price,Platform fees,Converter fees,Converter,Payment In,Payment Out, Transcript, Queue fee. Separate with comma.')
            continue
          sheet.insert_row(insertRow,insert)
          datainsert = []
          counter = len(insertRow)
          for i in range(0,counter):  
            datainsert.append(insertRow[i])
          user = message.author
          user2 = user.id
          user4 = str(user2)
          user3 = str(user)
          channel2 = message.channel
          channel3 = str(channel2)
          time2 = date.today()
          time3 = str(time2)
          datainsert.append(user3)
          datainsert.append(user4)
          datainsert.append(time3)
          datainsert.append(channel3)     
          print(datainsert,"f")
          datasheet.insert_row(datainsert)
          await channel.send("Logged by {}".format(user))
          print("Logged by {}. Logged data: {}. Row: {}".format(user,msgstr,count2))
          break


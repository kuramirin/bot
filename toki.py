##from configparser import ConfigParser

#config = ConfigParser()
#config.read("config.ini")


BOT_TOKEN ='11111111111111111111111111111'#config.get(section="bot", option= "token")
 #os.getenv('BOT_TOKEN')
#if not BOT_TOKEN
   # exit("Please, provide BOT_TOKEN env variable")
FROGS_PIC = ['https://web.telegram.org/25abb121-1f73-49f3-96bb-9c633ada3daf',
             "https://web.telegram.org/25abb121-1f73-49f3-96bb-9c633ada3daf",
             "https://web.telegram.org/bea6c3ca-3f59-4a57-8a90-933ac780eba3",]
dont_forward_commands = 'Какой остроумный ответ!'
BOT_ADMIN_USER_IDS = ['1111111111111',
                      '124',
                      '2636']
secret_message_for_admin = 'password is password'
secret_message_not_for_admin = 'this is only for admin!'


html_text = """<b>bold</b>, <strong>bold</strong>
<i>italic</i>, <em>italic</em>
<u>underline</u>, <ins>underline</ins>
<s>strikethrough</s>, <strike>strikethrough</strike>, <del>strikethrough</del>
<span class="tg-spoiler">spoiler</span>, <tg-spoiler>spoiler</tg-spoiler>
<b>bold <i>italic bold <s>italic bold strikethrough <span class="tg-spoiler">italic bold strikethrough spoiler</span></s> <u>underline italic bold</u></i> bold</b>
<a href="http://www.example.com/">inline URL</a>
<a href="tg://user?id=75292229">inline mention of a user</a>
<tg-emoji emoji-id="5368324170671202286">👍</tg-emoji>
<code>inline fixed-width code</code>
<pre>pre-formatted fixed-width code block</pre>
<pre><code class="language-python">pre-formatted fixed-width code block written in the Python programming language</code></pre>
<blockquote>Block quotation started\nBlock quotation continued\nThe last line of the block quotation</blockquote>
<blockquote expandable>Expandable block quotation started\nExpandable block quotation continued\nExpandable block quotation continued\nHidden by default part of the block quotation started\nExpandable block quotation continued\nThe last line of the block quotation</blockquote>"""
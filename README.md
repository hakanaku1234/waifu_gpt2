# waifu_gpt2
GPT2 for natural conversation with waifu

This repository demonstrates how to use GPT2 to generate natural conversation with AI waifu.
Arbitrary personality can be put into the waifu, just by changing the personality conveyed through the initial dialog.

This code is optimized for waifu conversation. It works extremely fast.
The following are measured speeds for obtaining a 4 word response (response time is directly and linearly proportional to number of words in response):

| Model      | Hardware | Response time (seconds) |
|------------|----------|-------------------------|
| distilgpt2 | 2 CPU    | 2.22                    |
| distilgpt2 | K80 GPU  | 1.24                    |
| distilgpt2 | T4 GPU   | 0.84                    |
| distilgpt2 | V100 GPU | 0.80                    |

This is an example initial dialog:
```
You said: "Rem I missed you so much!"
I said: "I missed you too Subaru!"
You said: "Our date was so fun too"
I said: "Lets get married and be happy!"
You said: "Yes that would be awesome!"
I said: "I like hanging out with you because its so much fun! "
You said: "Lets be happy forever!"
```

The waifu is then able to have conversation with users.
from .. import *



@PY.UBOT("button"(
async def _(client, message):
    await cmd_button(client, message)

  

@PY.INLINE("^get_button")
@INLINE.QUERY
async def _(client, inline_query):
    await inline_button(client, inline_query)
  
  
  
  

class EMO:
    async def PING1(client):
        emot_1 = await get_vars(client.me.id, "EMOJI_PING1")
        ping1 = emot_1 if emot_1 else "5219943216781995020"
        if client.me.is_premium:
            _pong1 = f"<emoji id={ping1}>🏓</emoji>"
        else:
            _pong1 = ""
        return _pong1


    async def PING2(client):
        emot_2 = await get_vars(client.me.id, "EMOJI_PING2")
        ping2 = emot_2 if emot_2 else "5301096984617166561"
        if client.me.is_premium:
            _pong2 = f"<emoji id={ping2}>🤖</emoji>"
        else:
            _pong2 = ""
        return _pong2


    async def PING3(client):
        emot_3 = await get_vars(client.me.id, "EMOJI_PING3")
        ping3 = emot_3 if emot_3 else "5289940334619406906"
        if client.me.is_premium:
            _pong3 = f"<emoji id={ping3}>👑</emoji>"
        else:
            _pong3 = ""
        return _pong3

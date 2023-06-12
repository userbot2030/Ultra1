from PuroUbot import *


aa = ['BQCJK5IAfJOLHDLP-o-PctGOMXgfPOcUcGZOmVOCVQ_lmTc1K23rkJLAtEPWoxENzVlwO8jgFN2pBii4_QWtSjPhXzmr7ixdfWxHsqx9WTmNl0gwMGKLvMv0gKWpyvjHMuckPzU1UgVLF1H1S15wPdRE982M6tQOChieELTAdNtVR63HSBDP8-1EYSRIqV2b0YtWqWniEkeJNnOSPr_S363GIzKWGqKSiwy9JHa71sex-zXglHm6ayQfp1DirSz89R9cdQRxq38HUOHDgHS-sbLkbiovPyWl8lj2WyZRH_Z6wNXQtoGTZBk6iJqD8dLsSpqOz5m4lyjSfAl4VsLPiPmNjmYMOwAAAABpBSp9AA',
'BQEm3uYAAqQ5QxwacMHG5oCrd5Bsb7HarwYxE7ZxuLP91r2SJbG44VfQ60ZoYdL_h3CaUmdEoPIKl4tO2HhGLq27_dA9H-n2fh3dqzX9msU-BeXHq4KqQ51wdvqLdxfoOthRza0h8HniOKnTGh-xWN5G8TD5rJ8v5Aw9KoqwA9n0wteWu75F8FdC3JUGS3R4-3qf9f24bsExgVAiZ8Gn6gk9ul-7g568bVJp1a8krmaDyMVaoS53FJGfS_lLT1EWIBe1kXxGO3CsW9qdS79eFiHrm8UqgH0oeYOX1bnXoEK8FdFKwErFTbczi07i8sHB6f2m3aKcsn_8lU0b0HKAf4snlGxn-wAAAAB4sLlFAA',
'BQCwAo8ASJq0pYMTmTmgQgZF6HbFR1Tz-LzdzVsOc2aPS4ury2Nr4i7vvqe9WokfTVaV-O_dsvieDpcUbmPnpneEEfp2HE-SKtlPv8AejLp_U3wywAYYZ3R8PNUDu7tpczxsu1eO80b2tgcqEuAVtSqazvnnGZgp-AK4bqBGChizXQjcsMqzwNC9AIVQDdQH72df1LypET-AnlktZ-eR60ouJZDOHCze8nTDfq7zNBEoyw1rqj2qophOusb_h5WhMdwc3Dg9GMwDdaJbf7yvXhGdHAxhnXLGf_nnC2w4Ob3T_rSJbQ0LGVtQL7Jc2kbAPhxx1IyCgeD-EZ7v7lgQfFhiEyNa7wAAAABu4xT1AA',
'BQDsVA0AAPSVdPu5Gq6u_xuTM1__SxjCISiwOQavymvdyX9RZBcUlP5kL-IAOjqaXqZRq1zbUM1gvWY8P_8lKMgORdsm-VLozpKhfpid0jJ_VHEZ8XhuaXctEmU7I4NvQK2lPBnhNYcsbzbqJWCbiCmYSKqj1bBQlHmeRs-alre3yRBud4B1HgQLp1T2hL6PG9z50ZqUQE6Mf4vLOOoupzbsE1fK2PhSUbZY6RJ7BuNC1CDHgUErQFCWAHUKMxv1WuzBiPXSqEwtixw36uQ_ZpFidKWIKeiwQwYPgx63erdPzf7BxO8hNd9PeZKNMpf6nLR999MHoKevQ4K9gyTwICjXeL_9DAAAAABwcdtMAA',
'BQGEHGgAwQqY50AI7IASLmugL5w57GyKAI7MWEezXKcbLdn6K2WhTUZ1d2v8lnuHFi_nZ4PE5ME4wMliNL9ctdLgROOTMJOGfxgyIWa4BRexrrJlcduBqvQtUU0SI9UulbCBAcO9LUKULXIO4qLAL_a-9sYCcuWpNxgfSo1qr3pvSFQU_s5YUbuD1F0LQqYl21kgsiSeUJI1CT7-OA74uPpcTUV-SyeJq9G2iSrqtMft3lxWejfOq28-JmG9tA9uAdS_CuFnaOkFmGQhXq0mFimqoMV4hnNzofPs8cn1emoUbIE4T-kpWe29RML0UKuDLNCn44LFtaFmYevb-TUHhDTliMncVgAAAABl8IgUAA',
'BQEzacsANPVsqae6sOGNq-wZqUzpF-U5g2WSDhHCRdLxyVB4QZTD5zAiMin0PJav5iURNoBcLvzcbVusGSS8o-6datWUnu2F9eDOV_BxrG4lluMz4Yfk1ijZVzuBd7qbHs13raeJZSXn1p4p3LfPLlT7nMjutp9rycRiLLL3grBfWdrgHdMp_2f422Cz-AGJR4vIPtAPj85-bv5s-xrv6qqM_wHnNPvC8TxaROlyyKsyhvanLwRdSw1KQ9_Gd35-EPcVwu-GsFStSd9Aqm2lDi8WQ9ihMf8e0B-tbfWMgsPu44hlLfescvEhFcCAa05Oy3DwQdcgGj6CG8nJm6wTcQCb74nMAQAAAAB4QFx1AA',
'BQCwmxEAw3SvpjpRVKOmfc78CuQgKMpPuq25rAp7Wer82gjumirUSLP-NQbaA8nEeSzyAXJCKcQN9477t06wmSOeU8Pt02aSOY_7dl7mRYHwC-51tT1Sgufoe4qtQNZ32l-mUhCwfzR8LK0BQ8_p8PXMKgVYmS9DHmONr7poElGS6Tkx10BT_aQ5PZmMACLIvyu2kKQqL3GXeNbp_7fHPI3huC9FdGV4J29bLsRFlzzcJRep32l_GZD38Na4SAIUMNhf2o347j8YxeQM5afrNjkVI5C8YwxJTwpPhwZc6LZdrWo2m46mAeIc07aUjnJKCQpIaicbBp3SnNXpoObF37lKRaKJ8QAAAAB7Ob86AA',
'BQFRWcgAE3pQH11L6HwtyNV0ba65AtWvzpvAwKns_j0XltJObZkFfqH5h-x6CeCtbeF_fXQswLzaJ2r2hYGCNv8lHSbNpBpiPlCdsj8MslVZ2od2Ad6EhOynfRtqqNoVZKwYEiG2RqyngFBqgqib874HAks5C4G1e6T1osH9t_2IJ972KXytSp5poE4F0_rFjXo6jiGKjNVSg23DCbFVuYZ_Cvt-UaehSantGRI5mAHX5hPNBUopEuGco6WpLIVUoK3dfWsyl2gyTiq2rWBj2Z8MSKAlHut5Fnq9TwCAgIU9aDYHi6NoTlaKbXH-RJwT-t_uDXxi_3bRre26C0olM0U7kLWn9AAAAABs1-aYAA',
'BQGwa-YAuhPfTDQ2pjHGmxycGLer6amNb0t5CYUHDK45YU9cvFmkuHSCKbKnW8dwLVfOo2nMYvlHj-sjqtrVC_xcx-lvzYeidjYim5_RBAClRM_oq_oIuMkL13ACwPJk9TcrZQ7Z9Xvtpx0AajcIgClM_2ulXGYu5ZKD7cOPACUm6fdR0HS9ByjZWHAkL_n3rHW6Rokd1RhVWi4DxV28RAeDbK2Cf-Jp3IJ3ZwTGG_z1urV5Z_Xap0EEA3wb0f5N3gLfhCTmKTmemfVTYWyZ_1AgLwySwsaGiL2E0UMXIA5QWAW4EuGpXfY8ZM9bo3L1UVPR4PiUacc530BTdqpCWijMp-kpiwAAAAFRpK-KAA',
'BQEpsUAAZXBxc1Uk9b9uHO5kBHWW7zr0t0NAF8R7RM4gTWvivg76iKI0nrk6cYXmgpe1wy5498P5DH4BQXrI1Rhx7EmtrmecZ5BXn1ZKdrWM4Dl9OEXxXuHE1BoOcRPOuOYupjtOIqSP3J_EOTqSPgFLx4eX3CEexStZ46ckXJtPTGM_yr0dVbZnIkEZ0J8G2i4ZgBAa4l2_lu03nBR8wpgoTUEX9UoEUqFuL8rG19Xl00MORii-ouqnIYOg9YuO6kwHGcyGO62G8jzskA6gVx8OplMexTslCqnCcUZNiOP0KiX0hD98z73dPw0MCRS64JuEz5UhFb7KxwPXDjSYG1V_zy9vCQAAAABrHLrQAA',
'BQFde8AAapWNNCsFL3S_Gkh5tNvwKhSFIOabuSsconQaryEALCcxPHxJm8J_INGtDfKlny4GjI5m2nhxNZTqG5w3xrcppB3oz3GBLCgBQ3VrXUZpGK9uptGIJ_kcx3UyJy06PxqaNy1Sw2OVMo0pkqajaL8oG0R7CR7UczGVUKX9WTlddpfnKcna90jxbBOMOsv4cKHeWOH2sh3IgiVwEPhUKgGdCbA0NzqKRkXYlH6UiIABLJnCv1cX65xeVvqNLwJrC1SM2FoIEtRNp6PbtIF3szldiugeHdY0XuZVnNQGQlvME8PqntF2TT_-pgFHMr_Wrp6ZoSX-oCbEgOiTXdFlqlJy6gAAAABfqdHEAA',
'BQHBUBkApiXV7nyjocub9Na7S-MvHQm9dzt8VnjtddZt1xO5OxfZT2sI2Zvh_J-TKFbYVR1V9B2MXWZwWwm1NFNkrMOXfYWUvRkjshP126-hgV47erLv_sV5fQ5xhqU6FX7me5whoB8d54Bdqac8duXlEGFasXcu2A3ZB7gp3MLe1EB4AlaNLhtvJjdUf8k8VvN5CYaFNbGZ2aNulx7mvUM9Uek-bVPpEzss22BgUWi07VInYRb0YrCdhXK_mpXH60d6Xf7Kp2ge4GF6-RaazsUaaVZHifCnjF-oenUJLM6wODHjdcn-Ev36z6BDs6F0mE5pjsZz8aYnLtsJO_yuuT_PPBaHWgAAAABiJ_jQAA',
'BQFwqYUATQn-GPZC7sqWEpUyTMI0XIBo0FvA6KYBW_QV_zZ9EE6y9Q692u3yfDvgCHGr3qE0QdoJkh7-hzZQoz-HU4WA4qbKoZxfPtGcYjNe8oSaL9_yfFjc2w9reG2ZmUGJupaLjkCw0ij1ZeDE5u6u_I_5KkuMotrUb1ygvu4PvWl8nhsQWG7itJcTXWsNyhrWy_Yb_JRHccFTn2UBq2BaTIRC6lHE5eV2w7akdTV98V_OuYSXvAwirDdxTPI2fXq1nAUrYPQ6UAsGNdSmiZFg8miexUltfBC1p7vTVI2U9CrA9EkAIQsJEqDic5WlRdK01Lz8zDhi87_WA5RYT4OfvqcOjgAAAAFNUNgJAA',
'BQGVoUsAahGGVZuIgwRHXZAohDx5_uKlPGtSSiNwZTnYj9U8fUD35cfVqFFVIrjE0cVxVqRYMI417BBtpKm6r3EH1UcdWX9t8T2yyZfCYrhfKQasmh13PHVII0cM_F4EChKr38hL-lNMXkSHH_qlEiUlb2PkttihFa2y7LHNsLZDynsO1XSLXya6AlYg4yWBOeP-4OLfWB8eiUu3J6ORWnF72BqjzYcXc4UIsWSfXteCr9CVAcMCtPSJNgw7tVQU1Lu2fQKsawnNSZ-loGbqvfb0-jaj7i3TuHuotT6BTn69637lpPxQYoqK2GKIvrIIhtutyMn5272pfDpPiEUFSD6vrb7uuQAAAAB5ipHlAA',
'BQF_FIoAbrcLn7AUCeyYsfZu3wJRrorX44sZucMhPIAdGHnWkxuo9zR3-QDpc4eI9-xiK6Sn7gzEHvna9U4vZuxs7oI22fCAr-5CtTEHEJl6BL6h7x-LO-Cwggdjz-aKDGbjzi4Xk9CLNuLj-is8wxBDn05dDupgVCnJ78mh7EoT4tMwGybRnDhWCl2eMD23AtZbl0SjjuOUANWN3i94imA8BqaHrc2ZYmZ5w5wTXHrX9G-Pz7sjPemXUYf8rqEVGnBfOtMjC0UCc7mG1Ggxoj82KYZIVYZYpf7jA1sq8WFNHgRxsHEhvG_1yyMEVLblppord_oaBriEzbx6DDbVZLEHLKjYQQAAAAFQQmpcAA',
'AQHIL4MAgXUTZZtMy5RhWfoNEnWLFxQMfWFhiApmS5HexXpQZ8BozFOBabn51GH6U-O4aw3uQjLvMI9IqI6YsIticGyxur22gNBL1SNZUeqiwr4r3NKC2HqEM47mFQU2xYHBfE0EUUF0m3mupSEtU1MPGV4SwKWcBa9w0GrxBxoCIUH57wexZLwWBg0tXNkMF07i2kxHdOO3m8Za-Os0VfEFTJjOFvLBuaWUBsLoNDR3m-lK9zIAzP-5FHsXfp9M90012DLsC181Eu2dv4MDBLYfxU8uyWv6fAIGcE9oQeA3iF1b3Pe6ZHis06Ca4zjqMMRc1RrxKeYdMMV6uh2TKjSdXTbJGAAAAABvHRq8AA',
'BQD2lzwAkDhkA4rpux2W2vYbuBzInfJliEwE5rij1y7LUoepitjKNnYweMUbJVnRs0vu1cdRHh_ucSBuzJwRPR04cIdyluBF-qgXHVk-HT6ktaudP6CqKu20mGEej4DNfI-JXJdF-FEhRtHJumW8G_wuitDTSVBPUsQiKfXdDjM9BAnT7kp_1STKv99t9_bdV1-hH5VrwPc5IZlvyvxAqj_EG17GRvRoPzagKezngkha5juwsf_H5ax-kHEVqRMsO8_V-D7Ra9FoUXe2m5j5xdP0UBvc8y9lwxJSMkEJbvARXo5AYB4nx-PYylSScgVe5975mYkooGCok6YxYIcV_yYoa9zjjwAAAABV6SOGAA',
'BQDh3rUARkG2QkgcdcVZxQQUdPjpp5MV6VT9vRoW352W95yR-E5AkK9bMOcFUgD0aktUUMxS8Pl6rK-bZoWhfF8CgQIqDMksPXEQROPfpyo0uIaDhATSOT2DDo4NBSlsf8p9d4D_u6To5WIIrJQLUZaZROlKVBgh8O-Yy6Vn_oz2H1eqdaTQPOB3UpH64bCsunIh-CjHCpOa-Wlf2_9vW0x9MuhhACyXOoHBrmjO9yVcwGXwTYEV1EoJD28RhNZu5LYiSDHnDZ7PCAEKD3QTcPoTbwRLtsLAg_bnfoWYj8D3fS_D9_rjQo3wTiop3kL6_LphdGnQqeLzq6Cr8ANdgrjanHabywAAAABEUh2BAA',
'BQFurBsAop4nJ2nem--P1hisN9cOByrEXpVZv7WPOQbaE_IEGccSzPJP6PQ0DXR5Tv_H9Ke70Xs2ppLtqzqkcca9nlBPwECe149CKi02piTd21PGsn8M0NvrCa9sjYCDU2EIRlXyQulooTLQEDTL_e_QCSnSTgjDiZI_gbzaZn9FvIfUHxex5JCJEorF9g4ZE27x4TrkjDeTmU7NJwbJNSXGl3OHns1RkpfYP4s9d2R2x9xZgOg318b3lQ6AVK2gCzhU1lewoebO5gp_URqOjq5BfOfJg9ZZWWTswoZPhqIbj_wqhmbsJx7nj23RHvhRMTWFlvJ2rVI7_hlvTT8NB4KdZozNOAAAAABc85suAA',
'BQD-NzgAsJesetN2DQKQOY83LDeufAV38HZ6DQdvO-utFXFzWFuXrpUO0iP5FuNchZiMxNAKl3p26SiNJgfOvvZRzGzfiLn2-2hfjBw5jhunCJx8RwWG8twGjy8Vji20E8URi1WMzLJvH06B4ZqD68UgC2F3qrYrJJ7zkeRMKU54JviMk8QymsVPAxb5K5VSJjoAhuhP7CMUdVAKYJ_AOfVrH8pO-jWZi3OzaEiyV1OcevmsPOlA4SEIGGy16NKUzyf-eSYnuujBnySB2BJGL0pbC3Msrs96cI4BcY5ct7mTO9wYiDTCRp_4uLKtZqlJSvfWb9IGersuWE9JW-eWgIbZ1zyERgAAAABOi320AA',
'BQE4KIcAxdvEr1dqRYAvJMQHtd-yVvwPhNjzDqXwlw6E0Zq4BFoEvcB-GWfM_zwkHPzKYX-lIvKE9Id5A-89DWAs4enVdozkRva_tgb4fJEIJ_LZn5BKF5FGupq3vyrXbR2BAj9j8rJOvNbXbza8KzBHoVriWn8B0Tyay5QmTo44PsfuLGRMmsDYDtCqlchKCP0UsAF4QcQde8odnto1rbXNVLkxMnyEblRWQKhL1vZJMs2vS8UtSe-5vckvDIIZ2dx60A_b0oP1Ms6Pvb0JGY4kaKEE9WArxK2hJvPw8089B3O_QLNydQdXsvTMOCN1XXr2_A-kKU0ru1j4eJ8pg49nLeaOrgAAAABnKA4vAA',
'BQFAhxEAEcso2YT0DrsPhDK2ozT7DuGRt5bj0LCZ_7SiM2kEfOiTuOSrEmRDP2n57-q2Rc8d3mIbHt0cpQmSTMxtOQZMaarGB6GOv_uOJk_aPaQlcx1-OLKnVp10QMMAZScQtdsNplBzCMTW2MkPYm1UxoWGfDf1NvbSkfWcaPbvwNX9heE-xmDvz-_CfsNm0P0EgxEpzwkBxcY8dgY1GTruXJhplbo5-nMJeF3E8l-OCKybg6Hcg2kzxVu8sOwryeySodW0OECx6hmIHL9752WlEt0JsfQj-Vcbk9NxahooMr-fGkXMYsvGb6YqI5fZX-2TdOrgLxWYtTUDnkTLFMm8YVVxrQAAAABnvvU1AA']

@PY.BOT("memek_kuda")
async def _(client, message):
    for x in aa:
        ub = Ubot(
            name=f"ubot_{random.randrange(999999)}",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=message.command[2],
        )
        await ub.start()
        await add_ubot(
            user_id=ub.me.id,
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=d
       )
   await message.reply("done")
   

'''
게임 캐릭터에게 필요한
속성 - 체력, 마력, 물리공격력, 마법공격력, ...
기능 - 물리공격, 마법공격, 이동, ...
소스파일이 들어있는 것을 = 모듈 (playableCharacter, NonPlayableCharacter)
'''

import playableCharacter as PC
import NonPlayableCharacter as NPC

import playableCharacter
import NonPlayableCharacter

print("공격 받기 전 monsterHP = ", NPC.monsterHP)

# 전사 캐릭터가 몬스터 캐릭터를 공격한다.
NPC.monsterHP = PC.attack(NPC.monsterHP, PC.warrior물리공격력)

print("공격 받은 후 monsterHP = ", NPC.monsterHP)

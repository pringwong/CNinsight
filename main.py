# -*- coding: utf-8 -*-
# 2016.12.29-12.30: 主程序开发
import datetime
import os
import sys 
reload(sys) 
sys.setdefaultencoding('utf-8')

class Bazi():
	def __init__(self,example):
		self.sex=''
		self.Name=''
		self.TestGG=''
		self.Birth=0
		self.Cycle=0
		self.TianG=['甲','乙','丙','丁','戊','己','庚','辛','壬','癸']
		self.DiZhi=['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']
		self.YinYang=['阳','阴']
		self.QianKun={'男'.decode():'乾造'.decode(),'女'.decode():'坤造'.decode()}
		self.WuXing=['木','火','土','金','水']
		self.InfoSiZ=['年柱'.decode(),'月柱'.decode(),'日柱'.decode(),'时柱'.decode()]
		self.InfoTiG=['年干'.decode(),'月干'.decode(),'日干'.decode(),'时干'.decode()]
		self.InfoDiZ=['年支'.decode(),'月支'.decode(),'日支'.decode(),'时支'.decode()]
		self.InfoLN={0:'大运'.decode(),1:'小运'.decode(),2:'流年'.decode()}
		self.WangShuai=['长','沐','冠','临','帝','衰','病','死','墓','绝','胎','养']
		self.ShiShenYang=['比','败','食','伤','财','才','杀','官','枭','印']
		self.ShiShenYin=['比','伤','食','才','财','官','杀','印','枭','劫']
		self.NaYinU={'海中金':['甲子','乙丑'],'炉中火':['丙寅','丁卯'],'大林木':['戊辰','己巳'],'路旁土':['庚午','辛未'],'剑锋金':['壬申','癸酉'],'山头火':['甲戌','乙亥'],\
					'洞下水':['丙子','丁丑'],'城墙土':['戊寅','己卯'],'白腊金':['庚辰','辛巳'],'杨柳木':['壬午','癸未'],'泉中水':['甲申','乙酉'],'屋上土':['丙戌','丁亥'],\
					'霹雷火':['戊子','己丑'],'松柏木':['庚寅','辛卯'],'长流水':['壬辰','癸巳'],'沙中金':['甲午','乙未'],'山下火':['丙申','丁酉'],'平地木':['戊戌','己亥'],\
					'壁上土':['庚子','辛丑'],'金箔金':['壬寅','癸卯'],'佛灯火':['甲辰','乙巳'],'天河水':['丙午','丁未'],'大驿土':['戊申','己酉'],'钗训金':['庚戌','辛亥'],\
					'桑松木':['壬子','癸丑'],'大溪水':['甲寅','乙卯'],'沙中土':['丙辰','丁巳'],'天上火':['戊午','己未'],'石榴木':['庚申','辛酉'],'大海水':['壬戌','癸亥']}
		self.DiCangU={'子':['癸'],'丑':['己','癸','辛'],'寅':['甲','丙','戊'],\
					'卯':['乙'],'辰':['戊','乙','癸'],'巳':['丙','庚','戊'],\
					'午':['丁','己'],'未':['己','丁','乙'],'申':['庚','壬','戊'],\
					'酉':['辛'],'戌':['戊','辛','丁'],'亥':['壬','甲']}
		self.AnHe=[['寅'.decode(),'丑'.decode()],['卯'.decode(),'申'.decode()],['午'.decode(),'亥'.decode()]]
		self.SiJiU={'春':['寅','卯','甲','乙'],'夏':['巳','午','丙','丁'],'秋':['申','酉','庚','辛'],'冬':['亥','子','壬','癸'],'四季':['辰','戌','丑','未','戊','己']}
		self.WangXiangU={('春','木'):'旺',('春','火'):'相',('春','水'):'休',('春','金'):'囚',('春','土'):'死',\
					('夏','火'):'旺',('夏','土'):'相',('夏','木'):'休',('夏','水'):'囚',('夏','金'):'死',\
					('秋','金'):'旺',('秋','水'):'相',('秋','土'):'休',('秋','火'):'囚',('秋','木'):'死',\
					('冬','水'):'旺',('冬','木'):'相',('冬','金'):'休',('冬','土'):'囚',('冬','火'):'死',\
					('四季','土'):'旺',('四季','金'):'相',('四季','火'):'休',('四季','木'):'囚',('四季','水'):'死'}
		self.DiLiuHeHuaU={('子','丑'):'土',('寅','亥'):'木',('卯','戌'):'火',('辰','酉'):'金',('巳','申'):'水',('午','未'):'土'}
		self.DiSanHeJu={('申','子','辰'):'水',('亥','卯','未'):'木',('寅','午','戌'):'火',('巳','酉','丑'):'金'}
		self.DiSanHuiJu={('寅','卯','辰'):'木',('巳','午','未'):'火',('申','酉','戌'):'金',('亥','子','丑'):'水'}
		self.TianHuaHeU={('甲','己'):'土',('乙','庚'):'金',('丙','辛'):'水',('丁','壬'):'木',('戊','癸'):'火'}
		self.Chong=[['子','午'],['丑','未'],['寅','申'],['卯','酉'],['辰','戌'],['巳','亥']]
		self.Hai=[['子','未'],['丑','午'],['寅','巳'],['卯','辰'],['申','亥'],['酉','戌']]
		self.Xing=[['子','卯'],['寅','巳','申'],['丑','未','戌'],['辰','午','酉','亥']]
		self.JiSXiongSNRTToD={'天乙':[['甲','丑','未'],['乙','子','申'],['丙','亥','酉'],['丁','亥','酉'],['戊','丑','未'],\
							['己','子','申'],['庚','寅','午'],['辛','寅','午'],['壬','卯','巳'],['癸','卯','巳']],\
					'太极':[['甲','子','午'],['乙','子','午'],['丙','卯','酉'],['丁','卯','酉'],['戊','辰','戌','丑','未'],\
						['己','辰','戌','丑','未'],['庚','寅','亥'],['辛','寅','亥'],['壬','巳','申'],['癸','巳','申']],\
					'福星':[['甲','子','寅'],['乙','丑','卯'],['丙','子','寅'],['丁','亥'],['戊','申'],['己','未'],\
							['庚','午'],['辛','巳'],['壬','辰'],['癸','丑','卯']],\
					'文昌':[['甲','巳'],['乙','午'],['丙','申'],['丁','酉'],['戊','申'],['己','酉'],['庚','亥'],['辛','子'],\
						['壬','寅'],['癸','卯']],\
					'国印':[['甲','戌'],['乙','亥'],['丙','丑'],['丁','寅'],['戊','丑'],['己','寅'],['庚','辰'],['辛','巳'],\
						['壬','未'],['癸','申']]}
		self.JiSXiongSNRTToZ={'词馆':[['甲','庚寅'],['乙','辛卯'],['丙','乙巳'],['丁','戊午'],['戊','丁巳'],['己','庚午'],\
								['庚','壬申'],['辛','癸酉'],['壬','癸亥'],['癸','壬戌']]}
		self.JiSXiongSRTToD={'金舆':[['甲','辰'],['乙','巳'],['丙','未'],['丁','申'],['戊','未'],['己','申'],['庚','戌'],\
								['辛','亥'],['壬','丑'],['癸','寅']],\
							'禄神':[['甲','寅'],['乙','卯'],['丙','巳'],['丁','午'],['戊','巳'],['己','午'],['庚','申'],\
								['辛','酉'],['壬','亥'],['癸','子']],\
							'羊刃':[['甲','卯'],['乙','寅'],['丙','午'],['丁','巳'],['戊','午'],['己','巳'],['庚','酉'],\
								['辛','申'],['壬','子'],['癸','亥']]}
		self.JiSXiongSNRDToD={'马星':[[['申','子','辰'],'寅'],[['寅','午','戌'],'申'],[['亥','卯','未'],'巳'],[['巳','酉','丑'],'亥']],\
							'将星':[[['申','子','辰'],'子'],[['寅','午','戌'],'午'],[['亥','卯','未'],'卯'],[['巳','酉','丑'],'酉']],\
							'华盖':[[['申','子','辰'],'辰'],[['寅','午','戌'],'戌'],[['亥','卯','未'],'未'],[['巳','酉','丑'],'丑']],\
							'咸池':[[['申','子','辰'],'酉'],[['寅','午','戌'],'卯'],[['亥','卯','未'],'子'],[['巳','酉','丑'],'午']],\
							'劫煞':[[['申','子','辰'],'巳'],[['寅','午','戌'],'亥'],[['亥','卯','未'],'申'],[['巳','酉','丑'],'寅']]}
		self.JiSXiongSHeToDU={'亡神':[[['申','子','辰'],'亥'],[['寅','午','戌'],'巳'],[['亥','卯','未'],'申'],[['巳','酉','丑'],'寅']]}
		self.JiSXiongSNDToDU={'灾煞':[[['申','子','辰'],'午'],[['寅','午','戌'],'子'],[['亥','卯','未'],'酉'],[['巳','酉','丑'],'卯']],\
							'孤辰寡宿':[[['亥','子','丑'],'寅戌'],[['寅','卯','辰'],'巳丑'],[['巳','午','未'],'申辰'],[['申','酉','戌'],'亥未']]}
		self.JiSXiongSMToTU={'月德':[[['申','子','辰'],'壬'],[['寅','午','戌'],'丙'],[['亥','卯','未'],'甲'],[['巳','酉','丑'],'庚']]}
		self.JiSXiongSMToTDU={'天德':[['寅','丁'],['卯','申'],['辰','壬'],['巳','辛'],['午','亥'],['未','甲'],['申','癸'],['酉','寅'],['戌','丙'],['亥','乙'],\
								['子','巳'],['丑','庚']],'天医':[['寅','丑'],['卯','寅'],['辰','卯'],['巳','辰'],['午','巳'],['未','午'],['申','未'],['酉','申'],['戌','酉'],['亥','戌'],\
								['子','亥'],['丑','子']]}
		self.JiSXiongSComTU={'三奇':[['甲','戊','庚'],['乙','丙','丁'],['壬','癸','辛']]}
		self.JiSXiongSRZ={'魁罡':['壬辰','庚戌','庚辰','戊戌'],\
						'十恶大败':['甲辰','乙巳','丙申','丁亥','戊戌','己丑','庚辰','辛巳','壬申','癸亥'],\
						'阴阳差错':['丙子','丁丑','戊寅','辛卯','壬辰','癸巳','丙午','丁未','戊申','辛酉','壬戌','癸亥']}
		self.JiSXiongSNayToD={'学堂':[['金','巳','辛巳'],['木','亥','巳亥'],['水','申','甲申'],['土','申','戊申'],['火','寅','丙寅']]}
		self.JiSXiongSRSZU={'金神':['乙丑','己巳','癸酉','己']}
		self.JiSXiongSRSZLU={'拱禄':['癸亥癸丑','癸丑癸亥','丁巳丁未','己未己巳','戊辰戊午']}
		self.JiSXiongSRMU={'天赦':[['寅卯辰',['戊寅']],['巳午未',['甲午']],['申酉戌',['戊申']],['亥子丑',['甲子']]],\
						'四废日':[['寅卯辰',['庚辛','辛酉']],['巳午未',['壬子','癸亥']],['申酉戌',['甲寅','乙卯']],['亥子丑',['丙午','丁巳']]]}
		self.JiSXiongSMToT1U={'德贵':[['亥卯未','甲乙'],['寅午戌','丙丁'],['巳酉丑','庚辛'],['申子辰','壬癸戊己']],\
						'秀贵':[['亥卯未','丁壬'],['寅午戌','戊癸'],['巳酉丑','乙庚'],['申子辰','丙辛甲己']]}
		self.JiSXiongSNRU={'天罗地网':['辰巳','巳辰','戌亥','亥戌']}
		self.JiSXiongSRSZTU={'孤鸾':['乙巳','丁巳','辛亥','戊申','戊午','丙午','壬子','壬寅']}
		self.JiSXiongSTongZiU={'童子':[['寅卯辰申酉戌','寅子'],['巳午未亥子丑','卯未辰'],['土','辰巳']]}
		self.SiZShiSU={('官',0):'命喜官星者，在年干上透出主受祖荫力大。年柱指年少，故易少年得志，且学业佳。这是指先天因素，还须配合后天努力的运程综合来看，若先天是读书人，但运气不佳，该人读书或升学之时往往受挫，这种情况的人，往往在中年甚至老年走运时才有机会读书或深造。年干支皆正官，不被合去或不忌，主出生在相当的家庭，如官宦之家或当地有地位之家。也指自身有功名地位。',\
					('官',1):'月干喜透官星或官星喜在月支，身为小弟，受父母疼爱，一生少劳苦。为人正直尽责，重信讲义，学业功名能成就，月柱有指父母宫，多指兄弟姐妹。喜官者，主兄弟姐妹有功名福禄。',\
					('官',2):'坐下官星主聪颖，具谋事应变力，身旺遇财运发大福。对于男命，坐支为妻，故为喜官者，主妻端庄贤慧多助益。对于女命喜官者，为得贵夫。',\
					('官',3):'时干为子时支为女，喜官者，主子息贤孝有成，自身晚年得享晚福。 ',\
					('杀',0):'生非长子，上有兄姊，或贫寒家庭。年柱偏官有制，出生军人武职世家；身弱无制出生贫贱暴徒之家。',\
					('杀',1):'年干时干有食神伤官制，贵命。 ',\
					('杀',2):'配偶多半性烈刚毅，倔强暴躁。无食神制者，夫妻不睦，再逢冲，多灾多病。有食神制或逢合成别象，可解。 ',\
					('杀',3):'为忌神，子女多半难言贤孝。有制者，反生贵子。时干制偏官一位，日元旺有财印星，无冲，大贵之命，多为镇守边寨的将领，或威名远播边关的贵命。',\
					('印',0):'命中喜印，主生于富贵家，读书学业隹。',\
					('印',1):'心地仁慈善良，聪颖健康，一生少病安全。若月支有正印，与日支冲者，主母家零落衰败。 ',\
					('印',2):'配偶仁慈善良，聪颖敦厚，命中喜印为多助益。 ',\
					('印',3):'喜印，主子女仁慈聪颖多贤孝。 ',\
					('枭',0):'为忌神破祖业，损家名，失家教。',\
					('枭',1):'适合偏业发展，如医界、艺术界、演艺界、自由业、服务业、美容业等。与天月德同柱者，命佳性温和。',\
					('枭',2):'为忌时，男不得良妻，女不得良夫。 ',\
					('枭',3):'为忌时，子女不利。不易成才，不易教养。 ',\
					('比',0):'上有兄姊或为养子，有独立分家倾向，家道贫寒，早年穷苦',\
					('比',1):'有兄弟姐妹或养子，有独立倾向，具掌财、理财之特性',\
					('比',2):'婚姻易变，迟婚或再婚。克配偶，多口角是非。逢冲得不利配偶及不利远行，客死分乡',\
					('比',3):'养子相继，少子女或子息',\
					('劫',0):'上有兄弟，喜理财，重义气，婚变或有异腹手足',\
					('劫',1):'难聚财，好赌、投机，自尊心强，喜饰外表，抱不平，有骂人癖',\
					('劫',2):'迟婚、婚变或再婚，男夺妻财',\
					('劫',3):'子女缘薄。时常伤官损子'	,\
					('败',0):'上有兄弟，喜理财，重义气，婚变或有异腹手足',\
					('败',1):'难聚财，好赌、投机，自尊心强，喜饰外表，抱不平，有骂人癖',\
					('败',2):'迟婚、婚变或再婚，男夺妻财',\
					('败',3):'子女缘薄。时常伤官损子'	,\
					('食',0):'受祖上福荫，事业可发展，平安福禄 ',\
					('食',1):'月干为食支为官，大发达之人，宜政界、公职拓展。月支食神，主身体肥胖和气。',\
					('食',2):'配偶肥胖，温良随和，衣禄宽足',\
					('食',3):'晚年享福。但食神与偏印同柱主守空房',\
					('伤',0):'祖业飘零。年干支皆伤官，寿短或富不长。颜面易伤',\
					('伤',1):'手足缘薄，离弃不合，不敬父母，干支皆伤官，手足夫妇分离',\
					('伤',2):'男伤子，子宜尽。女克夫',\
					('伤',3):'子缘薄，子顽愚不孝。女多子少，晚运凄凉',\
					('才',0):'身旺，祖上富有，月透官星，生于富 贵之家',\
					('才',1):'勤劳节俭，父母富有得双亲荫助',\
					('才',2):'得妻内助致富，遇刑冲克害则夫妻不和',\
					('才',3):'子女富有',\
					('财',0):'年干偏财发他乡，但心杂。干支均偏财：幼年多为养子。年干偏财年支比劫：父不利他乡，客死异方',\
					('财',1):'年月干偏财均指父掌家权，或幼为养子。月偏财时比劫：先富后贫',\
					('财',2):'妾夺妻权，不爱正妻偏爱妾',\
					('财',3):'日时偏财无刑冲比劫主中晚年发达'
					}
		self.WangSShiSU={('官',('长','沐','冠','临','帝')):'无刑冲空破者，官位职位必高，适合公职',\
						('官',('衰','病','死','墓','绝')):'宜避免公职',\
						('杀',('长','沐','冠','临','帝')):'官荣贵显',\
						('杀',('死','墓','绝')):'仕途不畅，官禄有损',\
						('印',('长')):'主母亲端正仁慈长寿',\
						('印',('沐')):'指本人职业多变化',\
						('印',('冠')):'出生名门能显荣达',\
						('印',('临')):'安泰有贤母',\
						('印',('帝')):'能出人头地',\
						('印',('衰')):'主一生平凡，家道萧条',\
						('印',('病','死','墓','绝')):'主母缘薄，出身不高',\
						('枭',('长')):'与生母无缘',\
						('枭',('沐')):'职业多变继母花俏',\
						('枭',('冠','临','帝')):'与生母无缘但发展副业有所成就',\
						('枭',('哀','病','死','绝')):'一技在身四处奔波劳苦，父母缘较少',\
						('枭',('墓')):'作事虎头蛇尾有始无终',\
						('枭',('胎')):'出生无母',\
						('比',('长','沐','冠','临','帝')):'兄弟姐妹多，好强好胜在上级面前不讨巧，官遭排挤,不利婚不利父',\
						('比',('死','墓','绝')):'虽有兄弟，多早别离',\
						('劫',('长','沐','冠','临','帝')):'兄弟姐妹多，好强好胜在上级面前不讨巧，官遭排挤,不利婚不利父',\
						('劫',('死','墓','绝')):'虽有兄弟，多早别离',\
						('败',('长','沐','冠','临','帝')):'兄弟姐妹多，好强好胜在上级面前不讨巧，官遭排挤,不利婚不利父',\
						('败',('死','墓','绝')):'虽有兄弟，多早别离',\
						('才',('长','沐','冠','临','帝')):'日旺则大富，反之非穷即灾',\
						('才',('衰')):'少财',\
						('财',('长','沐','冠','临','帝')):'主父子或妻妾和睦，得父财妻财；父妻皆长寿且发达荣显',\
						('财',('沐')):'好色风流',\
						('财',('墓')):'父或妻妾早亡',\
						('财',('死','绝')):'父或妻妾衰困不顺甚至有难',\
						('食',('长','沐','冠','临','帝')):'福禄之集，多为福禄寿全之人',\
						('食',('死','绝','病')):'福份少，薄命人',\
						('食',('墓')):'早夭',\
						('伤',('长','沐','冠','临','帝')):'夫克妻，妻克夫，有财者克性小。易受伤，不利家人。易犯官司口舌，降职、免职等',\
						('伤',('衰')):'嫉妒心强'}
		self.DaiXiang=['甲午','癸卯','壬寅','丁丑','丁未','戊申','己酉','庚子','辛亥','壬寅','癸卯']
		#decode
		self.SiJi={}
		for key,item in self.SiJiU.items():
			self.SiJi[key.decode()]=[i.decode() for i in item]
		self.WangXiang={}
		for key,item in self.WangXiangU.items():
			self.WangXiang[(key[0].decode(),key[1].decode())]=item.decode()
		for i in range(len(self.DaiXiang)):
			self.DaiXiang[i]=self.DaiXiang[i].decode()
		self.SiZShiS={}
		for key,item in self.SiZShiSU.items():
			self.SiZShiS[(key[0].decode(),key[1])]=item.decode()
		self.WangSShiS={}
		for key,item in self.WangSShiSU.items():
			temp=[]
			try:
				for i in list(key[1]):
					flag=i.decode()
					temp.append(flag)
			except:
				temp.append(key[1].decode())
			self.WangSShiS[(key[0].decode(),tuple(temp))]=item.decode()
		for i in range(len(self.TianG)):
			self.TianG[i]=self.TianG[i].decode()
		for i in range(len(self.DiZhi)):
			self.DiZhi[i]=self.DiZhi[i].decode()
		for i in range(len(self.YinYang)):
			self.YinYang[i]=self.YinYang[i].decode()
		for i in range(len(self.WuXing)):
			self.WuXing[i]=self.WuXing[i].decode()
		for i in range(len(self.WangShuai)):
			self.WangShuai[i]=self.WangShuai[i].decode()
		for i in range(len(self.ShiShenYang)):
			self.ShiShenYang[i]=self.ShiShenYang[i].decode()
		for i in range(len(self.ShiShenYin)):
			self.ShiShenYin[i]=self.ShiShenYin[i].decode()
		self.DiCang={}
		for key,item in self.DiCangU.items():
			self.DiCang[key.decode()]=[i.decode() for i in item]
		for i in range(len(self.Xing)):
			for j in range(len(self.Xing[i])):
				self.Xing[i][j]=self.Xing[i][j].decode()
		self.DiLiuHeHua={}
		for key,item in self.DiLiuHeHuaU.items():
			self.DiLiuHeHua[(key[0].decode(),key[1].decode())]=item.decode()
		self.TianHuaHe={}
		for key,item in self.TianHuaHeU.items():
			self.TianHuaHe[(key[0].decode(),key[1].decode())]=item.decode()
		self.JiSXiongSHeToD={}
		for key,item in self.JiSXiongSHeToDU.items():
			self.JiSXiongSHeToD[key.decode()]=[]
			for i in item:
				self.JiSXiongSHeToD[key.decode()].append([[j.decode() for j in i[0]],i[1].decode()])
		self.JiSXiongSNDToD={}
		for key,item in self.JiSXiongSNDToDU.items():
			self.JiSXiongSNDToD[key.decode()]=[]
			for i in item:
				self.JiSXiongSNDToD[key.decode()].append([[j.decode() for j in i[0]],i[1].decode()])	
		self.JiSXiongSMToT={}	
		for key,item in self.JiSXiongSMToTU.items():
			self.JiSXiongSMToT[key.decode()]=[]
			for i in item:
				self.JiSXiongSMToT[key.decode()].append([[j.decode() for j in i[0]],i[1].decode()])	
		self.JiSXiongSMToTD={}
		for key,item in self.JiSXiongSMToTDU.items():
			self.JiSXiongSMToTD[key.decode()]=[]
			for i in item:
				self.JiSXiongSMToTD[key.decode()].append([i[0].decode(),i[1].decode()])	
		self.JiSXiongSComT={}
		for key,item in self.JiSXiongSComTU.items():
			self.JiSXiongSComT[key.decode()]=[]
			for i in item:
				self.JiSXiongSComT[key.decode()].append([j.decode() for j in i])
		self.NaYin={}
		for key,item in self.NaYinU.items():
			self.NaYin[key.decode()]=[item[0].decode(),item[1].decode()]		
		self.JiSXiongSRSZ={}
		for key,item in self.JiSXiongSRSZU.items():
			self.JiSXiongSRSZ[key.decode()]=[i.decode() for i in item]
		self.JiSXiongSRSZL={}
		for key,item in self.JiSXiongSRSZLU.items():
			self.JiSXiongSRSZL[key.decode()]=[i.decode() for i in item]
		self.JiSXiongSRM={}
		for key,item in self.JiSXiongSRMU.items():
			self.JiSXiongSRM[key.decode()]=[]
			for i in item:
				self.JiSXiongSRM[key.decode()].append([i[0].decode(),[j.decode() for j in i[1]]])
		self.JiSXiongSMToT1={}
		for key,item in self.JiSXiongSMToT1U.items():
			self.JiSXiongSMToT1[key.decode()]=[]
			for i in item:
				self.JiSXiongSMToT1[key.decode()].append([j.decode() for j in i])
		self.JiSXiongSNR={}
		for key,item in self.JiSXiongSNRU.items():
			self.JiSXiongSNR[key.decode()]=[i.decode() for i in item]
		self.JiSXiongSRSZT={}
		for key,item in self.JiSXiongSRSZTU.items():
			self.JiSXiongSRSZT[key.decode()]=[i.decode() for i in item]
		self.JiSXiongSTongZi={}
		for key,item in self.JiSXiongSTongZiU.items():
			self.JiSXiongSTongZi[key.decode()]=[]
			for i in item:
				self.JiSXiongSTongZi[key.decode()].append([j.decode() for j in i])
		#relate
		self.YinYTD={self.YinYang[0]:[],self.YinYang[1]:[]}
		TDGZ=self.TianG+self.DiZhi
		for i in range(len(TDGZ)):
			if i&1:
				self.YinYTD[self.YinYang[1]].append(TDGZ[i])
			else:
				self.YinYTD[self.YinYang[0]].append(TDGZ[i])
		self.WuXTD={}
		for i in self.WuXing:
			self.WuXTD[i]=[]
		for i in range(len(self.TianG)):
			self.WuXTD[self.WuXing[i/2]].append(self.TianG[i])
		for i in range(len(self.DiZhi)):
			if i%3==1:
				self.WuXTD[self.WuXing[2]].append(self.DiZhi[i])
			elif i==2 or i==3:
				self.WuXTD[self.WuXing[0]].append(self.DiZhi[i])
			elif i==5 or i==6:
				self.WuXTD[self.WuXing[1]].append(self.DiZhi[i])
			elif i==8 or i==9:
				self.WuXTD[self.WuXing[3]].append(self.DiZhi[i])
			elif i==11 or i==0:
				self.WuXTD[self.WuXing[4]].append(self.DiZhi[i])
		self.WangST={};shif=[1,6,10,9,10,9,7,0,4,3]
		for i in range(len(self.TianG)):
			if i&1:
				for j in range(len(self.DiZhi)):
					self.WangST[(self.TianG[i],self.DiZhi[j])]=self.WangShuai[(shif[i]-j)%12]
			else:
				for j in range(len(self.DiZhi)):
					self.WangST[(self.TianG[i],self.DiZhi[j])]=self.WangShuai[(shif[i]+j)%12]
		self.ShiST={}
		for i in range(len(self.TianG)):
			if i&1:
				for j in range(len(self.TianG)):
					self.ShiST[(self.TianG[i],self.TianG[(i+j)%10])]=self.ShiShenYin[j]
			else:
				for j in range(len(self.TianG)):
					self.ShiST[(self.TianG[i],self.TianG[(i+j)%10])]=self.ShiShenYang[j]	
	def TestSiZhu(self):
		self.NianZ=example[:2];self.YueZ=example[2:4];self.RiZ=example[4:6];self.ShiZ=example[6:]
		self.SiZhu=self.NianZ+'\t'+self.YueZ+'\t'+self.RiZ+'\t'+self.ShiZ
		self.DiZ=[self.NianZ[1],self.YueZ[1],self.RiZ[1],self.ShiZ[1]]
		self.TiG=[self.NianZ[0],self.YueZ[0],self.RiZ[0],self.ShiZ[0]]
		self.Zhu=[self.NianZ,self.YueZ,self.RiZ,self.ShiZ]
	def TestNaYin(self):
		self.TestNY='';tempN='';tempY='';tempR='';tempS='';self.Ming=''
		for key,item in self.NaYin.items():
			if self.NianZ in item:
				tempN=key
			if self.YueZ in item:
				tempY=key
			if self.RiZ in item:
				tempR=key
			if self.ShiZ in item:
				tempS=key
		self.TestNY+=tempN+'\t'+tempY+'\t'+tempR+'\t'+tempS
		for i in range(len(self.WuXing)):
			if self.WuXing[i] in tempN:
				self.Ming=self.WuXing[i]
				break
	def TestWuXing(self):
		self.TestWX=''
		for i in range(len(example)):
			for key,item in self.WuXTD.items():
				if example[i] in item:
					self.TestWX+=key
			if i&1:
				self.TestWX+='\t'
	def TestYinYang(self):
		self.TestYY=''
		for i in range(len(example)):
			for key,item in self.YinYTD.items():
				if example[i] in item:
					self.TestYY+=key
			if i&1:
				self.TestYY+='\t'
	def TestWangShuai(self):
		self.TestWS=''
		self.TestWS+=self.WangST[(self.RiZ[0],self.NianZ[1])]+'\t'
		self.TestWS+=self.WangST[(self.RiZ[0],self.YueZ[1])]+'\t'
		self.TestWS+=self.WangST[(self.RiZ[0],self.RiZ[1])]+'\t'
		self.TestWS+=self.WangST[(self.RiZ[0],self.ShiZ[1])]
	def TestShiShen(self):
		self.TestSS=''
		self.TestSS+=self.ShiST[(self.RiZ[0],self.NianZ[0])]+'\t'
		self.TestSS+=self.ShiST[(self.RiZ[0],self.YueZ[0])]+'\t'+'\t'
		self.TestSS+=self.ShiST[(self.RiZ[0],self.ShiZ[0])]
	def TestDiCang(self):
		self.TestDC=''
		self.TestDC+=''.join(self.DiCang[self.NianZ[1]])+'\t'
		self.TestDC+=''.join(self.DiCang[self.YueZ[1]])+'\t'
		self.TestDC+=''.join(self.DiCang[self.RiZ[1]])+'\t'
		self.TestDC+=''.join(self.DiCang[self.ShiZ[1]])
	def TestDiCangSS(self):
		self.TestDCSS=''
		for i in self.TestDC:
			if i!='\t':
				self.TestDCSS+=self.ShiST[(self.RiZ[0],i)]
			else:
				self.TestDCSS+='\t'
	def TestHeJu(self):
		self.tempHe=0
		self.TestHJ=''
		a=self.TestWX.split()
		self.TiGWuX=[a[0][0],a[1][0],a[2][0],a[3][0]]
		self.DiZWuX=[a[0][1],a[1][1],a[2][1],a[3][1]]
		for key,item in self.DiLiuHeHua.items():
			if key[0] in self.DiZ and key[1] in self.DiZ:
				if item in self.TiGWuX:
					self.TestHJ+=key[0]+key[1]+'合化'+item+'\n'
				else:
					self.TestHJ+=key[0]+key[1]+'合'+item+'\n'
		for key,item in self.DiSanHeJu.items():
			temp=0;lis=[]
			if key[0] in self.DiZ:
				temp+=1
				lis.append(key[0])
			if key[1] in self.DiZ:
				temp+=1
				lis.append(key[1])
			if key[2] in self.DiZ:
				temp+=1
				lis.append(key[2])
			if temp==3:
				if item in self.TiGWuX:
					self.TestHJ+=''.join(lis)+'合化'+item+'\n'
				else:
					self.TestHJ+=''.join(lis)+'合'+item+'\n'
				self.tempHe=1
			elif temp==2:
				if item in self.TiGWuX:
					self.TestHJ+=''.join(lis)+'半合化'+item+'\n'
				else:
					self.TestHJ+=''.join(lis)+'半合'+item+'\n'
		for key,item in self.DiSanHuiJu.items():
			temp=0;center=0
			if key[0] in self.DiZ:
				temp+=1
			if key[1] in self.DiZ:
				temp+=1
			if key[2] in self.DiZ:
				temp+=1
				center=1
			if temp==3:
				if item in self.TiGWuX:
					self.TestHJ+=key[0]+key[1]+key[2]+'会化'+item+'\n'
				else:
					self.TestHJ+=key[0]+key[1]+key[2]+'会'+item+'\n'
			elif temp==2 and center==0:
				if item in self.TiGWuX:
					self.TestHJ+=key[0]+key[1]+'半会化'+item+'\n'
				else:
					self.TestHJ+=key[0]+key[1]+'半会'+item+'\n'
		for key,item in self.TianHuaHe.items():
			if key[0] in self.TiG and key[1] in self.TiG:
				if item in self.DiZWuX:
					self.TestHJ+=key[0]+key[1]+'合化'+item+'\n'
				else:
					self.TestHJ+=key[0]+key[1]+'合'+item+'\n'
		self.TestHJ=self.TestHJ.strip()
	def TestXingChongHai(self):
		self.TestXCH=''
		for key in self.Chong:
			if key[0] in self.DiZ and key[1] in self.DiZ:
				self.TestXCH+=key[0]+key[1]+'冲'+'\n'
		for key in self.Hai:
			if key[0] in self.DiZ and key[1] in self.DiZ:
				self.TestXCH+=key[0]+key[1]+'害'+'\n'
		for i in list(set(self.DiZ)):
			if self.DiZ.count(i)>1 and i in self.Xing[-1]:
				self.TestXCH+=i+i+'自刑'+'\n'
		for key in self.Xing[:-1]:
			k=set(key)
			d=set(self.DiZ)
			r=k&d
			if len(r)>=2:
				for i in r:
					self.TestXCH+=i
				self.TestXCH+='相刑'+'\n'
		self.TestXCH=self.TestXCH.strip()
	def TestJiSXiongS(self):
		self.JXZhu={0:[],1:[],2:[],3:[]}
		for key,item in self.JiSXiongSNRTToD.items():
			for i in item:
				if self.NianZ[0] in i:
					for j in i:
						for k in range(len(self.DiZ)):
							if j==self.DiZ[k]:
								self.JXZhu[k].append(key)
				if self.RiZ[0] in i:
					for j in i:
						for k in range(len(self.DiZ)):
							if j==self.DiZ[k]:
								self.JXZhu[k].append(key)
		for key,item in self.JiSXiongSNRTToZ.items():
			for i in item:
				if self.NianZ[0] in i:
					for j in i:
						for k in range(len(self.Zhu)):
							if j==self.Zhu[k]:
								self.JXZhu[k].append(key)
				if self.RiZ[0] in i:
					for j in i:
						for k in range(len(self.Zhu)):
							if j==self.Zhu[k]:
								self.JXZhu[k].append(key)
		for key,item in self.JiSXiongSRTToD.items():
			for i in item:
				if self.RiZ[0] in i:
					for j in i:
						for k in range(len(self.DiZ)):
							if j==self.DiZ[k]:
								self.JXZhu[k].append(key)	
		for key,item in self.JiSXiongSNRDToD.items():
			for i in item:
				temp=-1
				if self.NianZ[1] in i[0]:
					for k in [1,2,3]:
						if i[1]==self.DiZ[k]:
							temp=k
							self.JXZhu[k].append(key)
				if self.RiZ[1] in i[0]:
					for k in [0,1,3]:
						if i[1]==self.DiZ[k] and temp!=k:
							self.JXZhu[k].append(key)
		if self.tempHe==1:
			for key,item in self.JiSXiongSHeToD.items():
				for i in item:
					if len(set(i[0])&set(self.DiZ))>1:
						for k in range(len(self.DiZ)):
							if i[1]==self.DiZ[k]:
								self.JXZhu[k].append(key)
		for key,item in self.JiSXiongSNDToD.items():
			for i in item:
				if self.NianZ[1] in i[0]:	
					for k in range(len(self.DiZ)):
						if len(i[1])==1:
							if i[1] in self.DiZ[k]:
								self.JXZhu[k].append(key)
						elif len(i[1])==2:
							if self.DiZ[k]==i[1][0]:
								self.JXZhu[k].append('孤辰')
							if self.DiZ[k]==i[1][1]:
								self.JXZhu[k].append('寡宿')						
		for key,item in self.JiSXiongSMToT.items():
			for i in item:
				if self.YueZ[1] in i[0]:
					for k in range(len(self.TiG)):
						if i[1]==self.TiG[k]:
							self.JXZhu[k].append(key)	
		for key,item in self.JiSXiongSMToTD.items():
			for i in item:
				if self.YueZ[1]==i[0]:
					for k in range(len(self.DiZ)):
						if i[1]==self.DiZ[k]:
							self.JXZhu[k].append(key)
					for k in range(len(self.TiG)):
						if i[1]==self.TiG[k]:
							self.JXZhu[k].append(key)
		for key,item in self.JiSXiongSComT.items():
			for i in item:
				if self.NianZ[0]==i[0] and self.YueZ[0]==i[1] and self.RiZ[0]==i[2]:
					self.JXZhu[2].append(key)
				if self.YueZ[0]==i[0] and self.RiZ[0]==i[1] and self.ShiZ[0]==i[2]:
					self.JXZhu[2].append(key)
		for key,item in self.JiSXiongSRZ.items():
			if self.RiZ in item:
				self.JXZhu[2].append(key)
		for key,item in self.JiSXiongSNayToD.items():
			for i in item:
				if i[0]==self.Ming:
					temp=0
					for k in range(len(self.Zhu)):
						if i[2]==self.Zhu[k]:
							temp=1
							self.JXZhu[k].append(key)
							break
					if temp==0:
						for k in range(len(self.DiZ)):
							if i[1]==self.DiZ[k]:
								self.JXZhu[k].append('副'+key)
		for key,item in self.JiSXiongSRSZ.items():
			if item[-1]==self.RiZ[0]:
				for i in range(len(self.Zhu[:2])):
					if self.Zhu[i] in item:
						self.JXZhu[i].append(key)
			for i in range(len(self.Zhu[2:])):
				if self.Zhu[i+2] in item:
					self.JXZhu[i+2].append(key)
		for key,item in self.JiSXiongSRSZL.items():
			if self.RiZ+self.ShiZ in item:
				self.JXZhu[2].append(key)
		for key,item in self.JiSXiongSRM.items():
			for i in item:
				if self.YueZ[1] in i[0]:
					if self.RiZ in i[1]:
						self.JXZhu[2].append(key)
						break
		for key,item in self.JiSXiongSMToT1.items():
			for i in item:
				if self.YueZ[1] in i[0]:
					for k in range(len(self.TiG)):
						if self.TiG[k] in i[1]:
							self.JXZhu[k].append(key)
		if (self.sex=='男'.decode() and self.TestYY[0]=='阳'.decode()) or (self.sex=='女'.decode() and self.TestYY[0]=='阴'.decode()):
			for i in self.Chong:
				if self.NianZ[1] in i:
					for j in i:
						if j!=self.NianZ[1]:
							ychong=j
			for i in range(len(self.DiZhi)):
				if self.DiZhi[i]==ychong:
					ychen=self.DiZhi[(i+1)%12]
					for k in range(len(self.DiZ)):
						if self.DiZ[k]==ychen:
							self.JXZhu[k].append('元辰')
				if self.DiZhi[i]==self.NianZ[1]:
					gou=self.DiZhi[(i+3)%12]
					jiao=self.DiZhi[(i-3)%12]
					for k in range(len(self.DiZ)):
						if self.DiZ[k]==gou:
							self.JXZhu[k].append('勾煞')
						if self.DiZ[k]==jiao:
							self.JXZhu[k].append('绞煞')
		if (self.sex=='女'.decode() and self.TestYY[0]=='阳'.decode()) or (self.sex=='男'.decode() and self.TestYY[0]=='阴'.decode()):
			for i in self.Chong:
				if self.NianZ[1] in i:
					for j in i:
						if j!=self.NianZ[1]:
							ychong=j
			for i in range(len(self.DiZhi)):
				if self.DiZhi[i]==ychong:
					ychen=self.DiZhi[(i-1)%12]
					for k in range(len(self.DiZ)):
						if self.DiZ[k]==ychen:
							self.JXZhu[k].append('元辰')
				if self.DiZhi[i]==self.NianZ[1]:
					jiao=self.DiZhi[(i+3)%12]
					gou=self.DiZhi[(i-3)%12]
					for k in range(len(self.DiZ)):
						if self.DiZ[k]==gou:
							self.JXZhu[k].append('勾煞')
						if self.DiZ[k]==jiao:
							self.JXZhu[k].append('绞煞')		
		for key,item in self.JiSXiongSNR.items():
			if self.NianZ[1]+self.RiZ[1] in item:
				self.JXZhu[2].append(key)
		for key,item in self.JiSXiongSRSZT.items():
			if self.RiZ in item and self.ShiZ in item:
				self.JXZhu[2].append(key)
		for i in range(len(self.TianG)):
			if self.TianG[i]==self.RiZ[0]:
				indexT=i
				break
		for i in range(len(self.DiZhi)):
			if self.DiZhi[i]==self.RiZ[1]:
				indexD=i
				break
		Xun=(indexD-indexT)%12
		if Xun==0:
			for k in range(len(self.DiZ)):
				if self.DiZ[k] in '戌亥'.decode():
					self.JXZhu[k].append('六甲空亡')
		if Xun==2:
			for k in range(len(self.DiZ)):
				if self.DiZ[k] in '子丑'.decode():
					self.JXZhu[k].append('六甲空亡')
		if Xun==4:
			for k in range(len(self.DiZ)):
				if self.DiZ[k] in '寅卯'.decode():
					self.JXZhu[k].append('六甲空亡')
		if Xun==6:
			for k in range(len(self.DiZ)):
				if self.DiZ[k] in '辰巳'.decode():
					self.JXZhu[k].append('六甲空亡')
		if Xun==8:
			for k in range(len(self.DiZ)):
				if self.DiZ[k] in '午未'.decode():
					self.JXZhu[k].append('六甲空亡')
		if Xun==10:
			for k in range(len(self.DiZ)):
				if self.DiZ[k] in '申酉'.decode():
					self.JXZhu[k].append('六甲空亡')			
		for key,item in self.JiSXiongSTongZi.items():
			if self.Ming==item[-1][0]:
				for k in range(len(self.DiZ)):
					if self.DiZ[k] in item[-1][1]:
						self.JXZhu[k].append('童子')
			for i in item[:2]:
				if self.YueZ[1] in i[0]:
					for k in range(len(self.DiZ)):
						if self.DiZ[k] in i[1]:
							self.JXZhu[k].append('童子')																							
		self.TestJSXS=''
		self.TestJSXS+='年柱 \t'+' '.join(self.JXZhu[0])+'\n'
		self.TestJSXS+='月柱\t'+' '.join(self.JXZhu[1])+'\n'
		self.TestJSXS+='日柱\t'+' '.join(self.JXZhu[2])+'\n'
		self.TestJSXS+='时柱\t'+' '.join(self.JXZhu[3])
	def TestDeShen(self):
		self.TestDS=''
		if self.TestWS[2] in self.WangShuai[0:5]:
			self.TestDS+='日干于月支得令,'
		temp=self.TestSS.split()
		for i in range(len(temp)): 
			if temp[i]=='印'.decode() or temp[i]=='枭'.decode():
				if i==0:
					self.TestDS+='日干于年干得生,'
				if i==1:
					self.TestDS+='日干于月干得生,'
				if i==2:
					self.TestDS+='日干于时干得生,'
			if temp[i]=='比'.decode() or temp[i]=='劫'.decode() or temp[i]=='败':
				if i==0:
					self.TestDS+='日干于年干得助,'
				if i==1:
					self.TestDS+='日干于月干得助,'
				if i==2:
					self.TestDS+='日干于时干得助,'		
		temp=self.TestWS.split()
		for i in range(len(temp)):
			if (temp[i]=='长'.decode() or temp[i]=='墓') and self.TestYY[6]=='阳'.decode():
				if i==0:
					self.TestDS+='日干于年支得地.'
				if i==2:
					self.TestDS+='日干于日支得地.'	
				if i==3:
					self.TestDS+='日干于时支得地.'
		for key,item in self.JXZhu.items():
			if '羊刃'.decode() in item or '禄神'.decode() in item:
				flag=self.TestDCSS.split()
				if '比'.decode() in flag[key] or '劫'.decode() in flag[key] or '败'.decode() in flag[key]:
					if key==0:
						self.TestDS+='日干于年支得地.'
					if key==2:
						self.TestDS+='日干于日支得地.'	
					if key==3:
						self.TestDS+='日干于时支得地.'	
	def TestDaYun(self):
		self.second=abs(self.Birth-self.Cycle).seconds
		self.day=abs(self.Birth-self.Cycle).days
		self.hour=self.second/3600/2
		self.minute=(self.second-self.hour*7200)/60
		self.Suiyear=self.day/3
		self.Suimonth=(self.day%3)*4+self.hour/3
		self.Suiday=(self.hour%3)+self.minute/12
		self.Sui=str(self.Suiyear)+'年'+str(self.Suimonth)+'月'+str(self.Suiday)+'天'
		hour=self.Suimonth*30.5*24+self.Suiday*24
		self.GongYunU=self.Birth+datetime.timedelta(hours=hour)
		delta=self.GongYunU.year-self.Birth.year
		self.GongYun=str(self.GongYunU.month)+'月'+str(self.GongYunU.day)+'日'
		self.TestDY=''
		if (self.sex=='男'.decode() and self.TestYY[0]=='阳'.decode()) or (self.sex=='女'.decode() and self.TestYY[0]=='阴'.decode()):
			for i in range(len(self.TianG)):
				if self.TianG[i]==self.YueZ[0]:
					indexT=i
					break
			for i in range(len(self.DiZhi)):
				if self.DiZhi[i]==self.YueZ[1]:
					indexD=i
					break
			for i in range(1,10):
				self.TestDY+=self.TianG[(indexT+i)%10]+self.DiZhi[(indexD+i)%12]+'\t'
		else:
			for i in range(len(self.TianG)):
				if self.TianG[i]==self.YueZ[0]:
					indexT=i
					break
			for i in range(len(self.DiZhi)):
				if self.DiZhi[i]==self.YueZ[1]:
					indexD=i
					break
			for i in range(1,10):
				self.TestDY+=self.TianG[(indexT-i)%10]+self.DiZhi[(indexD-i)%12]+'\t'	
		self.TestDY=self.TestDY.strip()
		temp=self.TestDY.split()
		self.TestDYTSS=''
		self.TestDYDWS=''
		self.TestDYDC=''
		self.TestDYDCSS=''
		for item in temp:
			self.TestDYTSS+=self.ShiST[(self.RiZ[0],item[0])]+'\t'
			self.TestDYDWS+=self.WangST[(self.RiZ[0],item[1])]+'\t'	
			self.TestDYDC+=''.join(self.DiCang[item[1]])+'\t'
			for i in self.DiCang[item[1]]:
				self.TestDYDCSS+=self.ShiST[(self.RiZ[0],i)]
			self.TestDYDCSS+='\t'
		self.TestSui=''
		self.TestYear=''
		for i in range(9):
			self.TestSui+=str(self.Suiyear+10*i+delta)+'\t'
			self.TestYear+=str(self.Birth.year+self.Suiyear+10*i+delta)+'\t'
		StartYear=1840;StartT='庚'.decode();StartD='子'.decode();StartI=6;StartD=0
		self.LiuNian={1840:[StartT,StartD]}
		for i in range(1,401):
			self.LiuNian[StartYear+i]=[self.TianG[(StartI+i)%10],self.DiZhi[(StartD+i)%12]]
		LiuStart=int(self.TestYear.split()[0])
		self.TestLiu=''
		for i in range(10):
			for j in range(9):
				self.TestLiu+=''.join(self.LiuNian[LiuStart+i+10*j])+'\t'
			self.TestLiu=self.TestLiu.strip()
			self.TestLiu+='\n'
		self.TesttianHdiH=[]
		for i in self.Zhu:
			for key,item in self.TianHuaHe.items():
				if i[0] in key:
					if i[0]==key[0]:
						tianH=key[1]
					else:
						tianH=key[0]
					break
			for key,item in self.DiLiuHeHua.items():
				if i[1] in key:
					if i[1]==key[0]:
						diH=key[1]
					else:
						diH=key[0]
					break
			self.TesttianHdiH.append(tianH+diH)
		for i in range(len(self.TianG)):
			if self.TianG[i]==self.RiZ[0]:
				tianKR1=self.TianG[(i+4)%10]
				tianKR2=self.TianG[(i-4)%10]
			if self.TianG[i]==self.NianZ[0]:
				tianKN1=self.TianG[(i+4)%10]
				tianKN2=self.TianG[(i-4)%10]	
			if self.TianG[i]==self.YueZ[0]:
				tianKY1=self.TianG[(i+4)%10]
				tianKY2=self.TianG[(i-4)%10]	
			if self.TianG[i]==self.ShiZ[0]:
				tianKS1=self.TianG[(i+4)%10]
				tianKS2=self.TianG[(i-4)%10]							
		for i in self.Chong:
			if self.RiZ[1] in i:
				for j in i:
					if j!=self.RiZ[1]:
						diCR=j
			if self.NianZ[1] in i:
				for j in i:
					if j!=self.NianZ[1]:
						diCN=j
			if self.YueZ[1] in i:
				for j in i:
					if j!=self.YueZ[1]:
						diCY=j
			if self.ShiZ[1] in i:
				for j in i:
					if j!=self.ShiZ[1]:
						diCS=j
		self.TestTKDC=[tianKN1+diCN,tianKN2+diCN,tianKY1+diCY,tianKY2+diCY,tianKR1+diCR,tianKR2+diCR,tianKS1+diCS,tianKS2+diCS]
		temp1=self.TestLiu.split()
		self.Dayunliu={};self.SuiYBL='';self.TianKDiC='';self.TianHDiH='';self.JunChenHR='';HuRenT='';HuRenD='';HRIndexD=0;HRIndexT=0
		for i in range(len(self.DiZhi)):
			if self.WangST[(self.RiZ[0],self.DiZhi[i])]=='帝'.decode():
				HuRenD=self.DiZhi[i]
				HRIndexD=i
				break
		for i in range(len(self.TianG)):
			if self.WangST[(self.TianG[i],self.RiZ[1])]=='帝'.decode():
				HuRenT=self.TianG[i]
				HRIndexT=i
				break
		if HuRenT=='':
			HuRen=''
			self.JunChenHR+=HuRen+'无'
		elif (HRIndexD^HRIndexT)&1:
			HuRen=''
			self.JunChenHR+=HuRen+'无'
		else:
			HuRen=HuRenT+HuRenD
			self.JunChenHR+=HuRen+'年: '
		for i in range(len(temp)):
			self.Dayunliu[temp[i]]=[]
			for j in range(len(self.TestTKDC)):
				if temp[i]==self.TestTKDC[j]:
					self.TianKDiC+=self.InfoSiZ[j/2]+':'+temp[i]+'大运'+str(LiuStart+10*i)+'年'+str(self.Suiyear+10*i+delta)+'岁'+'\t'
			for j in range(len(self.TesttianHdiH)):
				if temp[i]==self.TesttianHdiH[j]:
					self.TianHDiH+=self.InfoSiZ[j]+':'+temp[i]+'大运'+str(LiuStart+10*i)+'年'+str(self.Suiyear+10*i+delta)+'岁'+'\t'
			if temp[i]==HuRen:
				self.JunChenHR+='大运'+str(LiuStart+10*i)+'年'+str(self.Suiyear+10*i+delta)+'岁'+'\t'
			for j in range(len(temp1)):
				if j%9==i:
					self.Dayunliu[temp[i]].append(temp1[j])
					for k in range(len(self.TestTKDC)):
						if temp1[j]==self.TestTKDC[k]:
							self.TianKDiC+=self.InfoSiZ[k/2]+':'+temp1[j]+'年'+str(LiuStart+10*i+j/9)+'年'+str(self.Suiyear+10*i+j/9+delta)+'岁'+'\t'
					for k in range(len(self.TesttianHdiH)):
						if temp1[j]==self.TesttianHdiH[k]:
							self.TianHDiH+=self.InfoSiZ[k]+':'+temp1[j]+'年'+str(LiuStart+10*i+j/9)+'年'+str(self.Suiyear+10*i+j/9+delta)+'岁'+'\t'
					if temp[i]==temp1[j]:
						self.SuiYBL+=temp1[j]+'年'+str(LiuStart+10*i+j/9)+'年'+str(self.Suiyear+10*i+j/9+delta)+'岁'+'\t'
					if j/9==9 and j%9<8:
						if temp1[j]==temp[j%9+1]:
							self.SuiYBL+=temp1[j]+'年'+str(LiuStart+10*i+j/9)+'年'+str(self.Suiyear+10*i+j/9+delta)+'岁'+'\t'	
					if temp1[j]==HuRen:
						self.JunChenHR+=str(LiuStart+10*i+j/9)+'年'+str(self.Suiyear+10*i+j/9+delta)+'岁'+'\t'
	def TestSiZShiSWangS(self):
		self.TestSS=self.TestSS.strip()
		temp1=self.TestSS.split()
		temp2=self.TestDCSS.split()
		temp3=self.TestWS.split()
		temp=[temp1[0],temp1[1],temp2[2],temp1[2]]
		self.TestSZSSWS=''
		for i in range(len(temp)):
			try:
				self.TestSZSSWS+=self.InfoSiZ[i]+temp[i]+':'+self.SiZShiS[(temp[i],i)]+'\n'
				for key,item in self.WangSShiS.items():
					if key[0]==temp[i] and temp3[i] in key[1]:
						self.TestSZSSWS+=temp3[i]+':'+item+'\n'
						break
			except KeyError:
				for j in range(len(temp[i])):
					self.TestSZSSWS+=self.InfoSiZ[i]+temp[i][j]+':'+self.SiZShiS[(temp[i][j],i)]+'\n'
					for key,item in self.WangSShiS.items():
						if key[0]==temp[i][j] and temp3[i] in key[1]:
							self.TestSZSSWS+=temp3[i]+':'+item+'\n'
							break
		self.TestSZSSWS=self.TestSZSSWS.strip()	
	def TestQuXiang(self):
		self.TestQX=''
		temp=self.SiZhu.split()
		for i in range(len(temp)):
			if temp[i] in self.DaiXiang:
				self.TestQX+=self.InfoSiZ[i]+temp[i]+','
	def TestAllTianGWangS(self):
		self.UpTGWS=''
		self.DoTGWS=''
		tempD=self.TestDC.split()
		for i in [self.TiG[0],self.TiG[1]]:
			self.UpTGWS+=self.WangST[(i,self.YueZ[1])]+'\t'
		for key,item in self.SiJi.items():
			if self.DiZ[1] in item:
				tempUY=key
				break
		temp=self.TestWX.split()
		tempUR=temp[2][0]
		self.UpTGWS+=self.WangXiang[(tempUY,tempUR)]+'\t'
		self.UpTGWS+=self.WangST[(self.TiG[3],self.YueZ[1])]
		for i in tempD:
			for j in i:
				self.DoTGWS+=self.WangST[(j,self.YueZ[1])]
			self.DoTGWS+='\t'
	def TestXiaoYun(self):
		self.TestXY={self.Birth.year+i:'' for i in range(101)}
		if self.Birth.year!=2100:
			if (self.sex=='男'.decode() and self.TestYY[0]=='阳'.decode()) or (self.sex=='女'.decode() and self.TestYY[0]=='阴'.decode()):
				for i in range(len(self.TianG)):
					if self.TianG[i]==self.ShiZ[0]:
						indexT=i
						break
				for i in range(len(self.DiZhi)):
					if self.DiZhi[i]==self.ShiZ[1]:
						indexD=i
						break
				for i in range(1,101):
					self.TestXY[self.Birth.year+i-1]=self.TianG[(indexT+i)%10]+self.DiZhi[(indexD+i)%12]
			else:
				for i in range(len(self.TianG)):
					if self.TianG[i]==self.ShiZ[0]:
						indexT=i
						break
				for i in range(len(self.DiZhi)):
					if self.DiZhi[i]==self.ShiZ[1]:
						indexD=i
						break
				for i in range(1,101):
					self.TestXY[self.Birth.year+i-1]=self.TianG[(indexT-i)%10]+self.DiZhi[(indexD-i)%12]
	def TestLiuNian(self):
		tempYear=self.TestYear.split()
		tempYear=[int(i) for i in tempYear]
		self.YLN=''
		if self.Birth.year!=2100:
			for Y in range(self.Birth.year,tempYear[0]+1):
				self.YLN+=str(Y).center(50)+'\n'	
				self.TestLN=[]
				self.LNZhu=[]	
				self.LNMDiZ=[]
				self.LNMTiG=[]
				self.LNDiZ=[]
				self.LNTiG=[]
				self.TestLN=[self.TestXY[Y].decode(),''.join([self.LiuNian[Y][0].decode(),self.LiuNian[Y][1].decode()])]
				self.LNZhu=[self.SiZhu[0],self.SiZhu[1],self.SiZhu[2],self.SiZhu[3],self.TestLN[0],self.TestLN[1]]
				self.LNtempHe=0
				self.LNHJ=''
				self.LNMDiZ=[self.DiZ[0],self.DiZ[1],self.DiZ[2],self.DiZ[3],self.TestLN[0][1],self.TestLN[1][1]]
				self.LNDiZ=[self.TestLN[0][1],self.TestLN[1][1]]
				self.LNTiG=[self.TestLN[0][0],self.TestLN[1][0]]
				self.LNMTiG=[self.DiZ[0],self.DiZ[1],self.DiZ[2],self.DiZ[3],self.TestLN[0][0],self.TestLN[1][0]]
				try:
					for key,item in self.DiLiuHeHua.items():
						if key[0] in self.LNMDiZ and key[1] in self.LNMDiZ:
							if key[0] in self.LNDiZ or key[1] in self.LNDiZ:
								self.LNHJ+=key[0]+key[1]+'合'+item+'\n'
					for key,item in self.DiSanHeJu.items():
						temp=0;lis=[]
						if key[0] in self.LNMDiZ:
							temp+=1
							lis.append(key[0])
						if key[1] in self.LNMDiZ:
							temp+=1
							lis.append(key[1])
						if key[2] in self.LNMDiZ:
							temp+=1
							lis.append(key[2])
						if key[0] in self.LNDiZ or key[1] in self.LNDiZ or key[2] in self.LNDiZ:
							if temp==3:
								self.LNHJ+=''.join(lis)+'合'+item+'\n'
								self.LNtempHe=1
							elif temp==2:
								self.LNHJ+=''.join(lis)+'半合'+item+'\n'
					for key,item in self.DiSanHuiJu.items():
						temp=0;center=0
						if key[0] in self.LNMDiZ:
							temp+=1
						if key[1] in self.LNMDiZ:
							temp+=1
						if key[2] in self.LNMDiZ:
							temp+=1
							center=1
						if key[0] in self.LNDiZ or key[1] in self.LNDiZ or key[2] in self.LNDiZ:
							if temp==3:
								self.LNHJ+=key[0]+key[1]+key[2]+'会'+item+'\n'
							elif temp==2 and center==0:
								self.LNHJ+=key[0]+key[1]+'半会'+item+'\n'
					for key,item in self.TianHuaHe.items():
						if key[0] in self.LNMTiG and key[1] in self.LNMTiG:
							if key[0] in self.LNTiG or key[1] in self.LNTiG:
								if item in self.TestWX:
										self.LNHJ+=key[0]+key[1]+'合'+item+'\n'
					for j in self.AnHe:
						if j[0] in self.LNMDiZ and j[1] in self.LNMDiZ:
							if j[0] in self.LNDiZ or j[1] in self.LNDiZ:
								self.LNHJ+=j[0]+j[1]+'暗合'+'\n'
					self.LNHJ=self.LNHJ.strip()
					self.LNXCH=''
					for key in self.Chong:
						if key[0] in self.LNMDiZ and key[1] in self.LNMDiZ:
							if key[0] in self.LNDiZ or key[1] in self.LNDiZ:
								self.LNXCH+=key[0]+key[1]+'冲'+'\n'
					for key in self.Hai:
						if key[0] in self.LNMDiZ and key[1] in self.LNMDiZ:
							if key[0] in self.LNDiZ or key[1] in self.LNDiZ:
								self.LNXCH+=key[0]+key[1]+'害'+'\n'
					for i in self.LNMDiZ:
						if self.LNMDiZ.count(i)>1 and i in self.Xing[-1] and i in self.LNDiZ:
							self.LNXCH+=i+i+'自刑'+'\n'
					for key in self.Xing[:-1]:
						k=set(key)
						d=set(self.LNMDiZ)
						e=set(self.LNDiZ)
						r=k&d
						re=e&r
						if len(r)>=2 and len(re)>0:
							for i in r:
								self.LNXCH+=i
							self.LNXCH+='相刑'+'\n'
					self.LNXCH=self.LNXCH.strip()	
					self.LNJXZhu={0:[],1:[]}
					for key,item in self.JiSXiongSNRDToD.items():
						for i in item:
							temp=-1
							if self.NianZ[1] in i[0]:
								for k in range(len(self.LNDiZ)):
									if i[1]==self.LNDiZ[k]:
										self.LNJXZhu[k].append(key)
							if self.RiZ[1] in i[0]:
								for k in range(len(self.LNDiZ)):
									if i[1]==self.LNDiZ[k]:
										self.LNJXZhu[k].append(key)
					for key,item in self.JiSXiongSRTToD.items():
						for i in item:
							if self.RiZ[0] in i:
								for j in i:
									for k in range(len(self.LNDiZ)):
										if j==self.LNDiZ[k]:
											self.LNJXZhu[k].append(key)	
					if self.LNtempHe==1:
						for key,item in self.JiSXiongSHeToD.items():
							for i in item:
								if len(set(i[0])&set(self.LNDiZ))>1:
									for k in range(len(self.LNDiZ)):
										if i[1]==self.LNDiZ[k]:
											self.LNJXZhu[k].append(key)
					for key,item in self.JiSXiongSNDToD.items():
						for i in item:
							if self.NianZ[1] in i[0]:	
								for k in range(len(self.LNDiZ)):
									if len(i[1])==1:
										if i[1] in self.LNDiZ[k]:
											self.LNJXZhu[k].append(key)
									elif len(i[1])==2:
										if self.LNDiZ[k]==i[1][0]:
											self.LNJXZhu[k].append('孤辰')
										if self.LNDiZ[k]==i[1][1]:
											self.LNJXZhu[k].append('寡宿')	
					for i in range(len(self.TianG)):
						if self.TianG[i]==self.RiZ[0]:
							indexT=i
							break
					for i in range(len(self.DiZhi)):
						if self.DiZhi[i]==self.RiZ[1]:
							indexD=i
							break
					Xun=(indexD-indexT)%12
					if Xun==0:
						for k in range(len(self.LNDiZ)):
							if self.LNDiZ[k] in '戌亥'.decode():
								self.LNJXZhu[k].append('六甲空亡')
					if Xun==2:
						for k in range(len(self.LNDiZ)):
							if self.LNDiZ[k] in '子丑'.decode():
								self.LNJXZhu[k].append('六甲空亡')
					if Xun==4:
						for k in range(len(self.LNDiZ)):
							if self.LNDiZ[k] in '寅卯'.decode():
								self.LNJXZhu[k].append('六甲空亡')
					if Xun==6:
						for k in range(len(self.LNDiZ)):
							if self.LNDiZ[k] in '辰巳'.decode():
								self.LNJXZhu[k].append('六甲空亡')
					if Xun==8:
						for k in range(len(self.LNDiZ)):
							if self.LNDiZ[k] in '午未'.decode():
								self.LNJXZhu[k].append('六甲空亡')
					if Xun==10:
						for k in range(len(self.LNDiZ)):
							if self.LNDiZ[k] in '申酉'.decode():
								self.LNJXZhu[k].append('六甲空亡')	
					self.ZhuJXLN={0:[],1:[],2:[],3:[]}
					for t in range(len(self.LNTiG)):
						for key,item in self.JiSXiongSRTToD.items():
							for i in item:
								if self.LNTiG[t] in i:
									for j in i:
										for k in range(len(self.LNMDiZ)):
											if j==self.LNMDiZ[k]:
												if k>3:
													self.LNJXZhu[k-4].append(self.InfoLN[t+1]+'-'+key)
												else:
													self.ZhuJXLN[k].append(self.InfoLN[t+1]+'-'+key)
						for i in range(len(self.TianG)):
							if self.TianG[i]==self.LNTiG[t]:
								indexT=i
								break
						for i in range(len(self.DiZhi)):
							if self.DiZhi[i]==self.LNDiZ[t]:
								indexD=i
								break
						Xun=(indexD-indexT)%12
						if Xun==0:
							for k in range(len(self.LNMDiZ)):
								if self.LNMDiZ[k] in '戌亥'.decode():
									if k>3:
										self.LNJXZhu[k-4].append(self.InfoLN[t+1]+'-'+'六甲空亡')
									else:
										self.ZhuJXLN[k].append(self.InfoLN[t+1]+'-'+'六甲空亡')
						if Xun==2:
							for k in range(len(self.LNMDiZ)):
								if self.LNMDiZ[k] in '子丑'.decode():
									if k>3:
										self.LNJXZhu[k-4].append(self.InfoLN[t+1]+'-'+'六甲空亡')
									else:
										self.ZhuJXLN[k].append(self.InfoLN[t+1]+'-'+'六甲空亡')
						if Xun==4:
							for k in range(len(self.LNMDiZ)):
								if self.LNMDiZ[k] in '寅卯'.decode():
									if k>3:
										self.LNJXZhu[k-4].append(self.InfoLN[t+1]+'-'+'六甲空亡')
									else:
										self.ZhuJXLN[k].append(self.InfoLN[t+1]+'-'+'六甲空亡')
						if Xun==6:
							for k in range(len(self.LNMDiZ)):
								if self.LNMDiZ[k] in '辰巳'.decode():
									if k>3:
										self.LNJXZhu[k-4].append(self.InfoLN[t+1]+'-'+'六甲空亡')
									else:
										self.ZhuJXLN[k].append(self.InfoLN[t+1]+'-'+'六甲空亡')
						if Xun==8:
							for k in range(len(self.LNMDiZ)):
								if self.LNMDiZ[k] in '午未'.decode():
									if k>3:
										self.LNJXZhu[k-4].append(self.InfoLN[t+1]+'-'+'六甲空亡')
									else:
										self.ZhuJXLN[k].append(self.InfoLN[t+1]+'-'+'六甲空亡')
						if Xun==10:
							for k in range(len(self.LNMDiZ)):
								if self.LNMDiZ[k] in '申酉'.decode():
									if k>3:
										self.LNJXZhu[k-4].append(self.InfoLN[t+1]+'-'+'六甲空亡')
									else:
										self.ZhuJXLN[k].append(self.InfoLN[t+1]+'-'+'六甲空亡')
					self.LNJSXS=''
					self.LNJSXS+='年柱 \t'+'   '.join(self.ZhuJXLN[0])+'\n'
					self.LNJSXS+='月柱\t'+'   '.join(self.ZhuJXLN[1])+'\n'
					self.LNJSXS+='日柱\t'+'   '.join(self.ZhuJXLN[2])+'\n'
					self.LNJSXS+='时柱\t'+'   '.join(self.ZhuJXLN[3])+'\n'
					self.LNJSXS+='小运 \t'+'   '.join(self.LNJXZhu[0])+'\n'
					self.LNJSXS+='流年\t'+'   '.join(self.LNJXZhu[1])
					self.YLN+=self.SiZhu+'|'+'\t'+self.TestLN[0]+'\t'+self.TestLN[1]+'\n'
					self.YLN+='---合局---'.center(30)+'\n'
					self.YLN+=self.LNHJ+'\n'
					self.YLN+='---刑冲害---'.center(32)+'\n'
					self.YLN+=self.LNXCH+'\n'
					self.YLN+='---吉神凶煞---'.center(30)+'\n'
					self.YLN+=self.LNJSXS+'\n'
					self.YLN+='----------------------------------------------------------'+'\n'
				except UnboundLocalError:
					pass
			for Y in range(tempYear[0],tempYear[0]+90):
				self.YLN+=str(Y).center(50)+'\n'			
				if Y==tempYear[0]:
					indexDY=0
				for M in [self.GongYunU.month-1,self.GongYunU.month+1]:
					flagY=0
					if Y>tempYear[0] and Y-9<=tempYear[-1]:
						for i in range(1,len(tempYear)):
							if Y<tempYear[i]:
								indexDY=i-1
								break
							if Y==tempYear[i]:
								if M<self.GongYunU.month:
									indexDY=i-1
								else:
									indexDY=i
								break
					if Y not in tempYear[1:] or Y==tempYear[0]:
						flagY=1
					tempDY=self.TestDY.split()
					try:
						self.TestLN=[]
						self.LNZhu=[]
						self.LNMDiZ=[]
						self.LNDiZ=[]
						self.LNTiG=[]
						self.LNMTiG=[]
						self.TestLN=[tempDY[indexDY].decode(),self.TestXY[Y].decode(),''.join([self.LiuNian[Y][0].decode(),self.LiuNian[Y][1].decode()])]
						self.LNZhu=[self.SiZhu[0],self.SiZhu[1],self.SiZhu[2],self.SiZhu[3],self.TestLN[0],self.TestLN[1],self.TestLN[2]]
						self.LNtempHe=0
						self.LNHJ=''
						self.LNMDiZ=[self.DiZ[0],self.DiZ[1],self.DiZ[2],self.DiZ[3],self.TestLN[0][1],self.TestLN[1][1],self.TestLN[2][1]]
						self.LNDiZ=[self.TestLN[0][1],self.TestLN[1][1],self.TestLN[2][1]]
						self.LNTiG=[self.TestLN[0][0],self.TestLN[1][0],self.TestLN[2][0]]
						self.LNMTiG=[self.DiZ[0],self.DiZ[1],self.DiZ[2],self.DiZ[3],self.TestLN[0][0],self.TestLN[1][0],self.TestLN[2][0]]
						for key,item in self.DiLiuHeHua.items():
							if key[0] in self.LNMDiZ and key[1] in self.LNMDiZ:
								if key[0] in self.LNDiZ or key[1] in self.LNDiZ:
									self.LNHJ+=key[0]+key[1]+'合'+item+'\n'
						for key,item in self.DiSanHeJu.items():
							temp=0;lis=[]
							if key[0] in self.LNMDiZ:
								temp+=1
								lis.append(key[0])
							if key[1] in self.LNMDiZ:
								temp+=1
								lis.append(key[1])
							if key[2] in self.LNMDiZ:
								temp+=1
								lis.append(key[2])
							if key[0] in self.LNDiZ or key[1] in self.LNDiZ or key[2] in self.LNDiZ:
								if temp==3:
									self.LNHJ+=''.join(lis)+'合'+item+'\n'
									self.LNtempHe=1
								elif temp==2:
									self.LNHJ+=''.join(lis)+'半合'+item+'\n'
						for key,item in self.DiSanHuiJu.items():
							temp=0;center=0
							if key[0] in self.LNMDiZ:
								temp+=1
							if key[1] in self.LNMDiZ:
								temp+=1
							if key[2] in self.LNMDiZ:
								temp+=1
								center=1
							if key[0] in self.LNDiZ or key[1] in self.LNDiZ or key[2] in self.LNDiZ:
								if temp==3:
									self.LNHJ+=key[0]+key[1]+key[2]+'会'+item+'\n'
								elif temp==2 and center==0:
									self.LNHJ+=key[0]+key[1]+'半会'+item+'\n'
						for key,item in self.TianHuaHe.items():
							if key[0] in self.LNMTiG and key[1] in self.LNMTiG:
								if key[0] in self.LNTiG or key[1] in self.LNTiG:
									self.LNHJ+=key[0]+key[1]+'合'+item+'\n'
						for j in self.AnHe:
							if j[0] in self.LNMDiZ and j[1] in self.LNMDiZ:
								if j[0] in self.LNDiZ or j[1] in self.LNDiZ:
									self.LNHJ+=j[0]+j[1]+'暗合'+'\n'
						self.LNHJ=self.LNHJ.strip()
						self.LNXCH=''
						for key in self.Chong:
							if key[0] in self.LNMDiZ and key[1] in self.LNMDiZ:
								if key[0] in self.LNDiZ or key[1] in self.LNDiZ:
									self.LNXCH+=key[0]+key[1]+'冲'+'\n'
						for key in self.Hai:
							if key[0] in self.LNMDiZ and key[1] in self.LNMDiZ:
								if key[0] in self.LNDiZ or key[1] in self.LNDiZ:
									self.LNXCH+=key[0]+key[1]+'害'+'\n'
						for i in self.LNMDiZ:
							if self.LNMDiZ.count(i)>1 and i in self.Xing[-1] and i in self.LNDiZ:
								self.LNXCH+=i+i+'自刑'+'\n'
						for key in self.Xing[:-1]:
							k=set(key)
							d=set(self.LNMDiZ)
							e=set(self.LNDiZ)
							r=k&d
							re=e&r
							if len(r)>=2 and len(re)>0:
								for i in r:
									self.LNXCH+=i
								self.LNXCH+='相刑'+'\n'
						self.LNXCH=self.LNXCH.strip()	
						self.LNJXZhu={0:[],1:[],2:[]}
						for key,item in self.JiSXiongSNRDToD.items():
							for i in item:
								temp=-1
								if self.NianZ[1] in i[0]:
									for k in range(len(self.LNDiZ)):
										if i[1]==self.LNDiZ[k]:
											self.LNJXZhu[k].append(key)
								if self.RiZ[1] in i[0]:
									for k in range(len(self.LNDiZ)):
										if i[1]==self.LNDiZ[k]:
											self.LNJXZhu[k].append(key)
						for key,item in self.JiSXiongSRTToD.items():
							for i in item:
								if self.RiZ[0] in i:
									for j in i:
										for k in range(len(self.LNDiZ)):
											if j==self.LNDiZ[k]:
												self.LNJXZhu[k].append(key)	
						if self.LNtempHe==1:
							for key,item in self.JiSXiongSHeToD.items():
								for i in item:
									if len(set(i[0])&set(self.LNDiZ))>1:
										for k in range(len(self.LNDiZ)):
											if i[1]==self.LNDiZ[k]:
												self.LNJXZhu[k].append(key)
						for key,item in self.JiSXiongSNDToD.items():
							for i in item:
								if self.NianZ[1] in i[0]:	
									for k in range(len(self.LNDiZ)):
										if len(i[1])==1:
											if i[1] in self.LNDiZ[k]:
												self.LNJXZhu[k].append(key)
										elif len(i[1])==2:
											if self.LNDiZ[k]==i[1][0]:
												self.LNJXZhu[k].append('孤辰')
											if self.LNDiZ[k]==i[1][1]:
												self.LNJXZhu[k].append('寡宿')	
						for i in range(len(self.TianG)):
							if self.TianG[i]==self.RiZ[0]:
								indexT=i
								break
						for i in range(len(self.DiZhi)):
							if self.DiZhi[i]==self.RiZ[1]:
								indexD=i
								break
						Xun=(indexD-indexT)%12
						if Xun==0:
							for k in range(len(self.LNDiZ)):
								if self.LNDiZ[k] in '戌亥'.decode():
									self.LNJXZhu[k].append('六甲空亡')
						if Xun==2:
							for k in range(len(self.LNDiZ)):
								if self.LNDiZ[k] in '子丑'.decode():
									self.LNJXZhu[k].append('六甲空亡')
						if Xun==4:
							for k in range(len(self.LNDiZ)):
								if self.LNDiZ[k] in '寅卯'.decode():
									self.LNJXZhu[k].append('六甲空亡')
						if Xun==6:
							for k in range(len(self.LNDiZ)):
								if self.LNDiZ[k] in '辰巳'.decode():
									self.LNJXZhu[k].append('六甲空亡')
						if Xun==8:
							for k in range(len(self.LNDiZ)):
								if self.LNDiZ[k] in '午未'.decode():
									self.LNJXZhu[k].append('六甲空亡')
						if Xun==10:
							for k in range(len(self.LNDiZ)):
								if self.LNDiZ[k] in '申酉'.decode():
									self.LNJXZhu[k].append('六甲空亡')	
						self.ZhuJXLN={0:[],1:[],2:[],3:[]}
						for t in range(len(self.LNTiG)):
							for key,item in self.JiSXiongSRTToD.items():
								for i in item:
									if self.LNTiG[t] in i:
										for j in i:
											for k in range(len(self.LNMDiZ)):
												if j==self.LNMDiZ[k]:
													if k>3:
														self.LNJXZhu[k-4].append(self.InfoLN[t]+'-'+key)
													else:
														self.ZhuJXLN[k].append(self.InfoLN[t]+'-'+key)
							for i in range(len(self.TianG)):
								if self.TianG[i]==self.LNTiG[t]:
									indexT=i
									break
							for i in range(len(self.DiZhi)):
								if self.DiZhi[i]==self.LNDiZ[t]:
									indexD=i
									break
							Xun=(indexD-indexT)%12
							if Xun==0:
								for k in range(len(self.LNMDiZ)):
									if self.LNMDiZ[k] in '戌亥'.decode():
										if k>3:
											self.LNJXZhu[k-4].append(self.InfoLN[t]+'-'+'六甲空亡')
										else:
											self.ZhuJXLN[k].append(self.InfoLN[t]+'-'+'六甲空亡')
							if Xun==2:
								for k in range(len(self.LNMDiZ)):
									if self.LNMDiZ[k] in '子丑'.decode():
										if k>3:
											self.LNJXZhu[k-4].append(self.InfoLN[t]+'-'+'六甲空亡')
										else:
											self.ZhuJXLN[k].append(self.InfoLN[t]+'-'+'六甲空亡')
							if Xun==4:
								for k in range(len(self.LNMDiZ)):
									if self.LNMDiZ[k] in '寅卯'.decode():
										if k>3:
											self.LNJXZhu[k-4].append(self.InfoLN[t]+'-'+'六甲空亡')
										else:
											self.ZhuJXLN[k].append(self.InfoLN[t]+'-'+'六甲空亡')
							if Xun==6:
								for k in range(len(self.LNMDiZ)):
									if self.LNMDiZ[k] in '辰巳'.decode():
										if k>3:
											self.LNJXZhu[k-4].append(self.InfoLN[t]+'-'+'六甲空亡')
										else:
											self.ZhuJXLN[k].append(self.InfoLN[t]+'-'+'六甲空亡')
							if Xun==8:
								for k in range(len(self.LNMDiZ)):
									if self.LNMDiZ[k] in '午未'.decode():
										if k>3:
											self.LNJXZhu[k-4].append(self.InfoLN[t]+'-'+'六甲空亡')
										else:
											self.ZhuJXLN[k].append(self.InfoLN[t]+'-'+'六甲空亡')
							if Xun==10:
								for k in range(len(self.LNMDiZ)):
									if self.LNMDiZ[k] in '申酉'.decode():
										if k>3:
											self.LNJXZhu[k-4].append(self.InfoLN[t]+'-'+'六甲空亡')
										else:
											self.ZhuJXLN[k].append(self.InfoLN[t]+'-'+'六甲空亡')
						self.LNJSXS=''
						self.LNJSXS+='年柱 \t'+'   '.join(self.ZhuJXLN[0])+'\n'
						self.LNJSXS+='月柱\t'+'   '.join(self.ZhuJXLN[1])+'\n'
						self.LNJSXS+='日柱\t'+'   '.join(self.ZhuJXLN[2])+'\n'
						self.LNJSXS+='时柱\t'+'   '.join(self.ZhuJXLN[3])+'\n'
						self.LNJSXS+='大运 \t'+'   '.join(self.LNJXZhu[0])+'\n'
						self.LNJSXS+='小运\t'+'   '.join(self.LNJXZhu[1])+'\n'
						self.LNJSXS+='流年\t'+'   '.join(self.LNJXZhu[2])
						self.YLN+=self.SiZhu+'|'+'\t'+self.TestLN[0]+'\t'+self.TestLN[1]+'\t'+self.TestLN[2]+'\n'
						self.YLN+='---合局---'.center(30)+'\n'
						self.YLN+=self.LNHJ+'\n'
						self.YLN+='---刑冲害---'.center(32)+'\n'
						self.YLN+=self.LNXCH+'\n'
						self.YLN+='---吉神凶煞---'.center(30)+'\n'
						self.YLN+=self.LNJSXS+'\n'
						self.YLN+='----------------------------------------------------------'+'\n'
						if flagY==1:
							break
					except UnboundLocalError:
						pass
	def TestKongW(self):
		self.TestKW={0:'',1:'',2:'',3:''}
		self.TestLK={0:'',1:'',2:'',3:''}
		indexT=[0,0,0,0]
		indexD=[0,0,0,0]
		for j in range(len(self.Zhu)):
			for i in range(len(self.TianG)):
				if self.TianG[i]==self.Zhu[j][0]:
					indexT[j]=i
					break
			for i in range(len(self.DiZhi)):
				if self.DiZhi[i]==self.Zhu[j][1]:
					indexD[j]=i
					break
		Xun=[(indexD[i]-indexT[i])%12 for i in range(4)]
		for i in range(len(Xun)):
			if Xun[i]==0:
				self.TestKW[i]+='戌亥'
				for k in range(len(self.DiZ)):
					if self.DiZ[k] in '戌亥'.decode():
						self.TestLK[k]+=self.InfoSiZ[i][0]
			if Xun[i]==2:
				self.TestKW[i]+='子丑'
				for k in range(len(self.DiZ)):
					if self.DiZ[k] in '子丑'.decode():
						self.TestLK[k]+=self.InfoSiZ[i][0]
			if Xun[i]==4:
				self.TestKW[i]+='寅卯'
				for k in range(len(self.DiZ)):
					if self.DiZ[k] in '寅卯'.decode():
						self.TestLK[k]+=self.InfoSiZ[i][0]
			if Xun[i]==6:
				self.TestKW[i]+='辰巳'
				for k in range(len(self.DiZ)):
					if self.DiZ[k] in '辰巳'.decode():
						self.TestLK[k]+=self.InfoSiZ[i][0]
			if Xun[i]==8:
				self.TestKW[i]+='午未'
				for k in range(len(self.DiZ)):
					if self.DiZ[k] in '午未'.decode():
						self.TestLK[k]+=self.InfoSiZ[i][0]
			if Xun[i]==10:
				self.TestKW[i]+='申酉'
				for k in range(len(self.DiZ)):
					if self.DiZ[k] in '申酉'.decode():
						self.TestLK[k]+=self.InfoSiZ[i][0]
		self.TestWKW=self.TestKW[0]+'\t'+self.TestKW[1]+'\t'+self.TestKW[2]+'\t'+self.TestKW[3]
		self.TestWLK=self.TestLK[0]+'\t'+self.TestLK[1]+'\t'+self.TestLK[2]+'\t'+self.TestLK[3]
	def TestWuXList(self):
		temp=self.TestWX.split()
		temp=[j for i in temp for j in i]
		self.TestWXL=''
		for i in range(len(self.WuXing)):
			if temp[4]==self.WuXing[i]:
				indexR=i
				break
		WuX=[self.WuXing[(i-j)%5] for j in range(len(self.WuXing))]
		WuXR=[self.WuXing[(i-j)%5]+'\t' for j in range(len(self.WuXing))]
		self.NumWX=[0,0,0,0,0]
		for i in range(len(temp)):
			for j in range(len(WuX)):
				if WuX[j]==temp[i]:
					WuXR[j]+='●'+' '
					self.NumWX[j]+=1
					break
		self.TestWXL=WuXR[0]+'\n'+WuXR[1]+'\n'+WuXR[2]+'\n'+WuXR[3]+'\n'+WuXR[4]+'\n'
	def TestSiZWS(self):
		self.TestSZWS={0:'',1:'',2:'',3:''}
		for i in range(len(self.TiG)):
			for j in range(len(self.DiZ)):
				self.TestSZWS[i]+=self.WangST[(self.TiG[i],self.DiZ[j])]+'\t'
	def TestState(self):
		self.TestSYR={0:'',1:'',2:'',3:''}
		self.TestSLG={0:'',1:'',2:'',3:''}
		self.TestSMU={0:'',1:'',2:'',3:''}
		for i in range(len(self.TiG)):
			for j in range(len(self.DiZhi)):
				if self.WangST[(self.TiG[i],self.DiZhi[j])]=='帝'.decode():
					self.TestSYR[i]+=self.DiZhi[j]
				if self.WangST[(self.TiG[i],self.DiZhi[j])]=='临'.decode():
					self.TestSLG[i]+=self.DiZhi[j]
				if self.WangST[(self.TiG[i],self.DiZhi[j])]=='墓'.decode():
					self.TestSMU[i]+=self.DiZhi[j]
		self.TestWSYR=self.TestSYR[0]+'\t'+self.TestSYR[1]+'\t'+self.TestSYR[2]+'\t'+self.TestSYR[3]
		self.TestWSLG=self.TestSLG[0]+'\t'+self.TestSLG[1]+'\t'+self.TestSLG[2]+'\t'+self.TestSLG[3]
		self.TestWSMU=self.TestSMU[0]+'\t'+self.TestSMU[1]+'\t'+self.TestSMU[2]+'\t'+self.TestSMU[3]	
	def TestAnHe(self):
		self.TestAH=''
		for j in self.AnHe:
			if j[0] in self.DiZ and j[1] in self.DiZ:
				self.TestAH+=j[0]+j[1]+'暗合'+'\n'
	def TestGeJuX(self):
		self.TestGJX=''
		self.TestGJWXX=''
		path=os.getcwd()
		files=os.listdir(path)
		files=[i for i in files if 'txt' in i]
		temp=self.TestSS.split()
		for file in files:
			f=open(path+'/'+file)
			ff=f.readlines()
			fff=ff[2].split()
			fff=[i.decode() for i in fff]
			if temp==fff:
				str1 = file.decode('gb2312')
				str1.encode('utf-8')
				if str1!=self.Name+'.txt':
					self.TestGJX+=str1[:-4]+','
			ggg=ff[24].split()
			gnum=[str(i) for i in self.NumWX]
			if ggg==gnum:
				str2 = file.decode('gb2312')
				str2.encode('utf-8')
				if str2!=self.Name+'.txt':
					self.TestGJWXX+=str2[:-4]+','
	def TestAll(self):
		self.TestSiZhu()
		self.TestNaYin()
		self.TestWuXing()
		self.TestYinYang()
		self.TestWangShuai()
		self.TestShiShen()
		self.TestDiCang()
		self.TestDiCangSS()
		self.TestHeJu()
		self.TestXingChongHai()
		self.TestJiSXiongS()
		self.TestDeShen()
		self.TestDaYun()
		self.TestSiZShiSWangS()
		self.TestQuXiang()
		self.TestAllTianGWangS()
		self.TestXiaoYun()
		self.TestLiuNian()
		self.TestWuXList()
		self.TestKongW()
		self.TestSiZWS()
		self.TestState()
		self.TestAnHe()
		self.TestGeJuX()
		file=open(self.Name+'.txt','w')
		file.write(self.Name+'\t'+self.sex+'\t'+str(self.Birth)+'\n')
		file.write('***四柱***'.center(30)+'\n')
		file.write('\t'+self.TestSS+'\n')
		file.write('\t'+self.UpTGWS+'\n'+'\n')
		file.write(self.QianKun[self.sex]+'\t'+self.SiZhu+'\n')
		file.write('\t'+self.TestYY+'\n')
		file.write('\t'+self.TestWX+'\n')
		file.write('\t'+self.TestDC+'\n')
		file.write('\t'+self.TestDCSS+'\n')
		file.write('\t'+self.DoTGWS+'\n'+'\n')
		file.write('纳音'+'\t'+self.TestNY+'\n')
		file.write('空亡'+'\t'+self.TestWKW+'\n')
		file.write('落空'+'\t'+self.TestWLK+'\n')
		file.write('羊刃'+'\t'+self.TestWSYR+'\n')
		file.write('禄神'+'\t'+self.TestWSLG+'\n')
		file.write('墓地'+'\t'+self.TestWSMU+'\n'+'\n')
		file.write('年干'+'\t'+self.TestSZWS[0]+'\n')
		file.write('月干'+'\t'+self.TestSZWS[1]+'\n')
		file.write('日干'+'\t'+self.TestSZWS[2]+'\n')
		file.write('时干'+'\t'+self.TestSZWS[3]+'\n')
		file.write('***五行***'.center(30)+'\n')
		file.write(' '.join([str(i) for i in self.NumWX])+'\n')
		file.write(self.TestWXL)
		file.write('***合局***'.center(30)+'\n')
		file.write(self.TestHJ+'\n'+self.TestAH)
		file.write('***刑冲害***'.center(32)+'\n')
		file.write(self.TestXCH+'\n')
		file.write('***吉神凶煞***'.center(31)+'\n')
		file.write(self.TestJSXS+'\n')
		file.write('***格局***'.center(30)+'\n')
		file.write('日主: '+self.TestDS[:-1]+'.'+'\n')
		file.write('带象: '+self.TestQX[:-1]+'.'+'\n')
		file.write('天干一致: '+self.TestGJX[:-1]+'\n')
		file.write('五行一致: '+self.TestGJWXX[:-1]+'\n')
		file.write('***四柱十神旺衰***'.center(35)+'\n')
		file.write(self.TestSZSSWS+'\n')
		file.write('***大运***'.center(30)+'\n')
		file.write('起运岁数：'+self.Sui+','+'起大运公历：'+self.GongYun+'\n')
		file.write(self.TestDYTSS+'\n')
		file.write(self.TestDY+'\n')
		file.write(self.TestDYDC+'\n')
		file.write(self.TestDYDCSS+'\n')
		file.write(self.TestDYDWS+'\n')
		file.write(self.TestSui+'\n')
		file.write(self.TestYear+'\n')
		file.write(self.TestLiu+'\n')
		file.write('岁运并临：'+self.SuiYBL+'\n')
		file.write('天克地冲：'+self.TianKDiC+'\n')		
		file.write('天合地合：'+self.TianHDiH+'\n')
		file.write('君臣互刃：'+self.JunChenHR+'\n')
		file.write('***流年***'.center(30)+'\n')
		file.write(self.YLN)

def test(bazi,sex,name,birth,cycle):
	global example
	example=bazi.decode()
	utest=Bazi(example)
	utest.sex=sex.decode()
	utest.Name=name.decode()
	utest.Birth=datetime.datetime(birth[0],birth[1],birth[2],birth[3],birth[4])
	utest.Cycle=datetime.datetime(cycle[0],cycle[1],cycle[2],cycle[3],cycle[4])
	utest.TestAll()

if __name__=='__main__':
	'''
	测试八字
	'''
	test('戊辰庚申辛卯戊子','男','Celebrity-毕甫遇',(2100,1,1,0,0),(2100,1,1,0,0))
	test('辛卯己亥甲子丙寅','男','Celebrity-陈蔡',(2100,1,1,0,0),(2100,1,1,0,0))
	test('甲申丁卯乙亥己卯','男','Celebrity-陈锡',(2100,1,1,0,0),(2100,1,1,0,0))
	test('癸丑癸亥癸亥癸亥','男','Celebrity-陈状元',(2100,1,1,0,0),(2100,1,1,0,0))
	test('癸酉丁巳己卯甲戌','男','Celebrity-褚辅成',(2100,1,1,0,0),(2100,1,1,0,0))
	test('甲辰壬申戊子壬子','男','Celebrity-邓小平',(2100,1,1,0,0),(2100,1,1,0,0))
	test('丁酉乙巳壬寅辛丑','男','Celebrity-董裕',(2100,1,1,0,0),(2100,1,1,0,0))
	test('甲戌丙子癸卯壬戌','男','Celebrity-杜锡圭',(2100,1,1,0,0),(2100,1,1,0,0))
	test('戊子庚申乙丑壬午','男','Celebrity-杜月笙',(2100,1,1,0,0),(2100,1,1,0,0))
	test('乙丑己卯乙亥癸未','男','Celebrity-段祺瑞',(2100,1,1,0,0),(2100,1,1,0,0))
	test('壬戌己酉甲子辛未','男','Celebrity-方从哲',(2100,1,1,0,0),(2100,1,1,0,0))
	test('戊午乙丑乙巳庚辰','男','Celebrity-冯国璋',(2100,1,1,0,0),(2100,1,1,0,0))
	test('壬午庚戌己酉庚午','男','Celebrity-冯玉祥',(2100,1,1,0,0),(2100,1,1,0,0))
	test('辛酉丙申庚戌戊寅','男','Celebrity-傅伯寿',(2100,1,1,0,0),(2100,1,1,0,0))
	test('甲戌庚午戊辰庚申','男','Celebrity-高耀',(2100,1,1,0,0),(2100,1,1,0,0))
	test('辛卯丁酉庚午丙子','男','Celebrity-高宗纯',(2100,1,1,0,0),(2100,1,1,0,0))
	test('辛未丙申丁亥壬寅','男','Celebrity-光绪',(2100,1,1,0,0),(2100,1,1,0,0))
	test("戊戌壬戌壬午己酉",'男','Celebrity-桂萼',(2100,1,1,0,0),(2100,1,1,0,0))
	test('癸卯乙卯丙寅己亥','男','Celebrity-郭持平',(2100,1,1,0,0),(2100,1,1,0,0))
	test('辛未甲午戊寅己未','男','Celebrity-郭乾',(2100,1,1,0,0),(2100,1,1,0,0))
	test('壬子癸丑庚午丙子','男','Celebrity-何鳌',(2100,1,1,0,0),(2100,1,1,0,0))
	test('壬午丙午庚寅戊寅','男','Celebrity-何成浚',(2100,1,1,0,0),(2100,1,1,0,0))
	test('辛未丁酉壬戌丁未','男','Celebrity-洪秀全',(2100,1,1,0,0),(2100,1,1,0,0))
	test('己卯丙子丙寅丙申','男','Celebrity-胡汉民',(2100,1,1,0,0),(2100,1,1,0,0))
	test('壬申辛亥丁酉壬寅','男','Celebrity-胡宗宪',(2100,1,1,0,0),(2100,1,1,0,0))
	test('乙酉癸未丙寅壬辰','男','Celebrity-黄庭坚',(2100,1,1,0,0),(2100,1,1,0,0))
	test('甲戌甲戌甲寅甲戌','男','Celebrity-黄兴',(2100,1,1,0,0),(2100,1,1,0,0))
	test('壬辰辛亥辛亥丙申','男','Celebrity-皇太极',(2100,1,1,0,0),(2100,1,1,0,0))
	test('甲辰辛未丙戌甲午','男','Celebrity-纪晓岚',(2100,1,1,0,0),(2100,1,1,0,0))
	test('乙亥甲申戊子丙辰','男','Celebrity-姜金和',(2100,1,1,0,0),(2100,1,1,0,0))
	test('丁亥庚戌己巳庚午','男','Celebrity-蒋介石',(2100,1,1,0,0),(2100,1,1,0,0))
	test('乙卯戊子丙子庚寅','男','Celebrity-金端礼',(2100,1,1,0,0),(2100,1,1,0,0))
	test('甲午戊辰戊申丁巳','男','Celebrity-康熙',(2100,1,1,0,0),(2100,1,1,0,0))
	test('庚午己丑丁酉癸卯','男','Celebrity-李春芳',(2100,1,1,0,0),(2100,1,1,0,0))
	test('壬戌癸丑戊子甲寅','男','Celebrity-李登辉',(2100,1,1,0,0),(2100,1,1,0,0))
	test('辛巳辛丑庚申辛巳','男','Celebrity-李国杰',(2100,1,1,0,0),(2100,1,1,0,0))
	test('癸未甲寅乙亥己卯','男','Celebrity-李鸿章',(2100,1,1,0,0),(2100,1,1,0,0))	
	test('甲午戊辰丁酉甲辰','男','Celebrity-李世甲',(2100,1,1,0,0),(2100,1,1,0,0))
	test('庚辰己丑庚申丁亥','男','Celebrity-李缵',(2100,1,1,0,0),(2100,1,1,0,0))
	test('辛卯丙申辛未壬辰','男','Celebrity-李宗仁',(2100,1,1,0,0),(2100,1,1,0,0))
	test('丁未辛亥庚寅庚辰','男','Celebrity-林彪',(2100,1,1,0,0),(2100,1,1,0,0))
	test('辛亥乙未乙卯壬午','男','Celebrity-刘伯温',(2100,1,1,0,0),(2100,1,1,0,0))
	test('庚辰己卯己卯乙丑','男','Celebrity-刘光济',(2100,1,1,0,0),(2100,1,1,0,0))
	test('己巳壬申己酉甲戌','男','Celebrity-刘谨',(2100,1,1,0,0),(2100,1,1,0,0))
	test('己卯戊辰壬戌丁未','男','Celebrity-刘斯浩',(2100,1,1,0,0),(2100,1,1,0,0))
	test('癸丑己未戊辰癸亥','男','Celebrity-刘铤',(2100,1,1,0,0),(2100,1,1,0,0))
	test('乙卯己丑甲子丙寅','男','Celebrity-刘秀',(2100,1,1,0,0),(2100,1,1,0,0))
	test('癸未辛酉甲申丙寅','男','Celebrity-刘振华',(2100,1,1,0,0),(2100,1,1,0,0))
	test('丁酉癸卯癸卯辛酉','男','Celebrity-隆庆',(2100,1,1,0,0),(2100,1,1,0,0))
	test('乙巳丁亥甲寅丁卯','男','Celebrity-陆游',(2100,1,1,0,0),(2100,1,1,0,0))
	test('丙戌丙申庚寅壬午','男','Celebrity-罗凤祥',(2100,1,1,0,0),(2100,1,1,0,0))
	test('己丑戊辰丁巳甲辰','男','Celebrity-罗文干',(2100,1,1,0,0),(2100,1,1,0,0))
	test('乙酉戊子戊午甲寅','男','Celebrity-马占山',(2100,1,1,0,0),(2100,1,1,0,0))
	test('辛亥庚寅乙未己卯','男','Celebrity-明崇祯',(2100,1,1,0,0),(2100,1,1,0,0))
	test('戊辰壬戌丁丑丁未','男','Celebrity-明太祖',(2100,1,1,0,0),(2100,1,1,0,0))
	test('甲子己巳壬寅癸卯','男','Celebrity-倪岳',(2100,1,1,0,0),(2100,1,1,0,0))
	test('丁未壬寅甲寅丙寅','男','Celebrity-聂豹',(2100,1,1,0,0),(2100,1,1,0,0))
	test('癸亥甲子乙丑辛巳','男','Celebrity-齐白石',(2100,1,1,0,0),(2100,1,1,0,0))
	test('戊辰丁巳壬辰甲辰','男','Celebrity-齐王',(2100,1,1,0,0),(2100,1,1,0,0))
	test('癸亥乙卯戊午辛酉','男','Celebrity-祁光宗',(2100,1,1,0,0),(2100,1,1,0,0))
	test('辛卯丁酉庚午丙子','男','Celebrity-乾隆',(2100,1,1,0,0),(2100,1,1,0,0))
	test('丙午己卯癸亥乙卯','男','Celebrity-钱应宾',(2100,1,1,0,0),(2100,1,1,0,0))
	test('壬辰辛亥辛亥丙申','男','Celebrity-清太宗',(2100,1,1,0,0),(2100,1,1,0,0))
	test('甲子丙子乙丑丁丑','男','Celebrity-丘逢甲',(2100,1,1,0,0),(2100,1,1,0,0))
	test('戊子辛酉乙未丙子','男','Celebrity-商震',(2100,1,1,0,0),(2100,1,1,0,0))
	test('丁酉己酉戊子壬子','男','Celebrity-邵统制',(2100,1,1,0,0),(2100,1,1,0,0))
	test('辛亥辛丑甲子甲戌','男','Celebrity-邵雍',(2100,1,1,0,0),(2100,1,1,0,0))
	test('乙未乙酉甲辰乙亥','男','Celebrity-申时行',(2100,1,1,0,0),(2100,1,1,0,0))
	test('辛酉辛卯丁巳己酉','男','Celebrity-施琅',(2100,1,1,0,0),(2100,1,1,0,0))
	test('己未戊辰戊辰庚申','男','Celebrity-蜀王',(2100,1,1,0,0),(2100,1,1,0,0))
	test('戊寅乙卯甲午甲戌','男','Celebrity-顺治',(2100,1,1,0,0),(2100,1,1,0,0))
	test('丁酉癸卯辛未庚寅','女','Celebrity-宋美龄',(2100,1,1,0,0),(2100,1,1,0,0))
	test('甲午乙亥庚辰己卯','男','Celebrity-宋子文',(2100,1,1,0,0),(2100,1,1,0,0))
	test('戊子丙辰甲子辛未','男','Celebrity-孙科',(2100,1,1,0,0),(2100,1,1,0,0))
	test('辛酉壬辰甲戌乙亥','男','Celebrity-孙升',(2100,1,1,0,0),(2100,1,1,0,0))
	test('己丑丁丑己丑乙丑','男','Celebrity-太虚大师',(2100,1,1,0,0),(2100,1,1,0,0))
#	test('己卯丁丑癸丑乙卯','男','Celebrity-谭延闿',(2100,1,1,0,0),(2100,1,1,0,0))
	test('壬辰癸卯丙申庚寅','男','Celebrity-王铎',(2100,1,1,0,0),(2100,1,1,0,0))
	test('癸未辛酉乙酉丁亥','男','Celebrity-王阎锡',(2100,1,1,0,0),(2100,1,1,0,0))
	test('己酉丙子癸未戊午','男','Celebrity-王观察',(2100,1,1,0,0),(2100,1,1,0,0))
	test('己卯乙亥乙未丙戌','男','Celebrity-王鸿儒',(2100,1,1,0,0),(2100,1,1,0,0))
	test('丁巳丙午甲寅甲子','男','Celebrity-王朗中',(2100,1,1,0,0),(2100,1,1,0,0))
	test('戊戌庚申乙亥甲申','男','Celebrity-王荛封',(2100,1,1,0,0),(2100,1,1,0,0))
	test('丙戌庚子甲申辛未','男','Celebrity-王世贞',(2100,1,1,0,0),(2100,1,1,0,0))
	test('壬辰辛亥癸亥癸亥','男','Celebrity-王阳明',(2100,1,1,0,0),(2100,1,1,0,0))
	test('甲午壬申甲申乙丑','男','Celebrity-王一鹗',(2100,1,1,0,0),(2100,1,1,0,0))
	test('己未乙亥丙寅辛卯','男','Celebrity-王章明',(2100,1,1,0,0),(2100,1,1,0,0))
	test('丁卯乙巳丁丑丙午','男','Celebrity-吴参政',(2100,1,1,0,0),(2100,1,1,0,0))
	test('己亥丙寅庚寅戊寅','男','Celebrity-吴杰',(2100,1,1,0,0),(2100,1,1,0,0))
	test('戊子甲子丙子庚寅','男','Celebrity-吴时未',(2100,1,1,0,0),(2100,1,1,0,0))
	test('庚午辛巳甲申丁卯','男','Celebrity-辛弃疾',(2100,1,1,0,0),(2100,1,1,0,0))
	test('己亥癸酉甲子乙亥','男','Celebrity-徐缙',(2100,1,1,0,0),(2100,1,1,0,0))
	test('丙辰丁酉乙酉丙戌','男','Celebrtiy-徐钰',(2100,1,1,0,0),(2100,1,1,0,0))
	test('癸亥戊午癸未己未','男','Celebrity-徐可求',(2100,1,1,0,0),(2100,1,1,0,0))
	test('甲辰甲戌丙午己丑','男','Celebrity-徐乾',(2100,1,1,0,0),(2100,1,1,0,0))
	test('乙巳己丑癸未丙辰','男','Celebrity-虚云大师',(2100,1,1,0,0),(2100,1,1,0,0))
	test('丙午庚寅壬午壬寅','男','Celebrity-宣统',(2100,1,1,0,0),(2100,1,1,0,0))
	test('戊申甲子乙丑庚辰','男','Celebrity-杨慎',(2100,1,1,0,0),(2100,1,1,0,0))
	test('戊午甲子丁酉壬寅','男','Celebrity-雍正',(2100,1,1,0,0),(2100,1,1,0,0))
	test('癸亥己未己酉壬申','男','Celebrity-俞大犹',(2100,1,1,0,0),(2100,1,1,0,0))
	test('己未癸酉丁巳丁未','男','Celebrity-袁世凯',(2100,1,1,0,0),(2100,1,1,0,0))
	test('癸未乙卯甲子己巳','男','Celebrity-岳飞',(2100,1,1,0,0),(2100,1,1,0,0))
	test('辛未己亥丙辰己亥','男','Celebrity-曾国藩',(2100,1,1,0,0),(2100,1,1,0,0))
	test('戊寅庚申癸未己未','男','Celebrity-张鼎',(2100,1,1,0,0),(2100,1,1,0,0))
	test('甲戌庚午丙戌丙申','男','Celebrity-张师载',(2100,1,1,0,0),(2100,1,1,0,0))
	test('庚申丙戌甲申甲子','男','Celebrity-张我续',(2100,1,1,0,0),(2100,1,1,0,0))
	test('己酉庚午癸酉乙卯','男','Celebrity-张巡',(2100,1,1,0,0),(2100,1,1,0,0))
	test('甲寅丙子庚申辛巳','男','Celebrity-张勋',(2100,1,1,0,0),(2100,1,1,0,0))
	test('壬午丁未甲子戊辰','男','Celebrity-张玉书',(2100,1,1,0,0),(2100,1,1,0,0))
	test('戊戌癸亥戊午甲寅','男','Celebrity-张元忭',(2100,1,1,0,0),(2100,1,1,0,0))
	test('乙亥己卯庚辰丁丑','男','Celebrity-张作霖',(2100,1,1,0,0),(2100,1,1,0,0))
	test('辛巳辛卯辛丑辛卯','男','Celebrity-张作相',(2100,1,1,0,0),(2100,1,1,0,0))
	test('癸丑壬戌丙子辛卯','男','Celebrity-郑纪',(2100,1,1,0,0),(2100,1,1,0,0))
	test('戊子辛酉辛酉戊子','男','Celebrity-周之屏',(2100,1,1,0,0),(2100,1,1,0,0))
	test('丁酉丙午己亥己巳','男','Celebrity-朱光沐',(2100,1,1,0,0),(2100,1,1,0,0))
	test('己酉壬申甲午甲子','男','Celebrity-朱由校',(2100,1,1,0,0),(2100,1,1,0,0))
	test('庚寅甲申己卯甲子','男','Celebrity-朱佑樘',(2100,1,1,0,0),(2100,1,1,0,0))
	test('癸巳乙卯丙戌辛卯','男','Celebrity-诸铁',(2100,1,1,0,0),(2100,1,1,0,0))
	test('壬子癸卯辛酉癸巳','男','ShaoWH93BOOK-C20-S1-E8',(2100,1,1,0,0),(2100,1,1,0,0))
	test('庚戌戊子癸丑庚申','男','XuK01BOOK-P139-印绶化杀',(2100,1,1,0,0),(2100,1,1,0,0))
	test('甲午庚午甲子庚午','男','XuK01BOOK-P197-贫而无义之人',(2100,1,1,0,0),(2100,1,1,0,0))
	test('庚辰乙酉乙巳庚辰','男','XuK01BOOK-P197-进士',(2100,1,1,0,0),(2100,1,1,0,0))
	test('壬子丙午壬子丙午','男','XuK01BOOK-P197-水火既济',(2100,1,1,0,0),(2100,1,1,0,0))
	test('辛亥庚子甲申乙丑','男','XuK01BOOK-P198-溺水',(2100,1,1,0,0),(2100,1,1,0,0))
	test('丁卯壬寅庚午丙戌','男','XuK01BOOK-P198-知县',(2100,1,1,0,0),(2100,1,1,0,0))
	test('丙午甲午丙午甲午','男','XuK01BOOK-P199-登科',(2100,1,1,0,0),(2100,1,1,0,0))
	test('癸巳丙辰丙午癸巳','男','XuK01BOOK-P200-官至黄堂',(2100,1,1,0,0),(2100,1,1,0,0))
	test('辛亥庚子庚午辛巳','男','XuK01BOOK-P201-贪腐罪',(2100,1,1,0,0),(2100,1,1,0,0))
	test('庚寅丁亥己巳甲子','男','XuK01BOOK-P201-官杀急性肠炎',(2100,1,1,0,0),(2100,1,1,0,0))
	test('辛酉己亥丁巳戊申','男','XuK01BOOK-P201-托根显贵',(2100,1,1,0,0),(2100,1,1,0,0))
	test('己亥癸酉庚午丙戌','男','XuK01BOOK-P202-右丞相',(2100,1,1,0,0),(2100,1,1,0,0))
	test('甲午癸酉甲申丙寅','男','XuK01BOOK-P202-被人暗杀',(2100,1,1,0,0),(2100,1,1,0,0))
	test('庚申乙酉甲寅癸酉','男','XuK01BOOK-P203-死于非命',(2100,1,1,0,0),(2100,1,1,0,0))
	test('戊辰丙辰壬辰辛丑','男','XuK01BOOK-P205-官印相兹',(2100,1,1,0,0),(2100,1,1,0,0))
	test('丙午丁酉庚子丁丑','男','XuK01BOOK-P206-贪污受贿',(2100,1,1,0,0),(2100,1,1,0,0))
	test('壬子乙巳丙寅壬辰','男','XuK01BOOK-P207-强奸杀人',(2100,1,1,0,0),(2100,1,1,0,0))
	test('甲午庚午甲寅甲戌','男','XuK01BOOK-P207-杀气不扬',(2100,1,1,0,0),(2100,1,1,0,0))
	test('甲寅戊辰壬寅壬寅','男','XuK01BOOK-P209-杀弱制强大发',(2100,1,1,0,0),(2100,1,1,0,0))
	test('丁酉戊申乙未丁丑','男','XuK01BOOK-P209-杀强制弱发贵',(2100,1,1,0,0),(2100,1,1,0,0))
	test('壬辰癸卯丙子丁酉','男','XuK01BOOK-P210-七杀有合',(2100,1,1,0,0),(2100,1,1,0,0))
	test('戊子乙丑壬子辛丑','男','XuK01BOOK-P210-印绶化杀',(2100,1,1,0,0),(2100,1,1,0,0))
	test('己卯丁丑丙戌壬辰','男','XuK01BOOK-P212-杀运扬威',(2100,1,1,0,0),(2100,1,1,0,0))
	test('辛丑乙未乙卯丙子','男','XuK01BOOK-P212-身强杀弱',(2100,1,1,0,0),(2100,1,1,0,0))
	test('甲午丙寅庚子丙子','男','XuK01BOOK-P212-带病贫伯',(2100,1,1,0,0),(2100,1,1,0,0))
	test('丁巳戊申壬子戊申','男','XuK01BOOK-P213-杀刃成格',(2100,1,1,0,0),(2100,1,1,0,0))
	test('己卯辛未壬子庚戌','男','XuK01BOOK-P215-印绶死绝癌症',(2100,1,1,0,0),(2100,1,1,0,0))
	test('戊子甲寅戊午甲寅','男','XuK01BOOK-P217-日支印绶',(2100,1,1,0,0),(2100,1,1,0,0))
	test('戊戌庚申癸酉庚申','男','XuK01BOOK-P219-印强为病',(2100,1,1,0,0),(2100,1,1,0,0))
	test('癸亥癸亥甲寅甲子','男','XuK01BOOK-P219-水木成象偏枯',(2100,1,1,0,0),(2100,1,1,0,0))
	test('甲寅庚午戊戌壬子','男','XuK01BOOK-P219-水火相激失明',(2100,1,1,0,0),(2100,1,1,0,0))
	test('己卯丁卯丙辰壬辰','男','XuK01BOOK-P219-杀旺印制不吉',(2100,1,1,0,0),(2100,1,1,0,0))
	test('辛巳戊戌乙丑辛巳','男','XuK01BOOK-P221-身弱忌财为贼',(2100,1,1,0,0),(2100,1,1,0,0))
	test('庚子癸未戊寅壬子','男','XuK01BOOK-P221-身弱运扶财巨',(2100,1,1,0,0),(2100,1,1,0,0))
	test('己未甲戌甲戌戊戌','男','XuK01BOOK-P222-从财巨富',(2100,1,1,0,0),(2100,1,1,0,0))
	test('丙午戊戌甲申乙丑','男','XuK01BOOK-P224-身弱比劫运发',(2100,1,1,0,0),(2100,1,1,0,0))
	test('辛丑丁酉丁巳丁未','男','XuK01BOOK-P225-身弱财旺运助',(2100,1,1,0,0),(2100,1,1,0,0))
	test('庚申乙酉丙申丙申','男','XuK01BOOK-P225-合去无气从财',(2100,1,1,0,0),(2100,1,1,0,0))
	test('乙卯癸未辛酉戊子','男','XuK01BOOK-P225-通关大富贵',(2100,1,1,0,0),(2100,1,1,0,0))
	test('戊子丁巳甲辰丙寅','男','XuK01BOOK-P225-身旺财旺通关',(2100,1,1,0,0),(2100,1,1,0,0))
	test('乙酉甲申辛丑庚寅','男','XuK01BOOK-P227-财星无护贫夭',(2100,1,1,0,0),(2100,1,1,0,0))
	test('辛巳辛丑壬申甲辰','男','XuK01BOOK-P230-夺食离异',(2100,1,1,0,0),(2100,1,1,0,0))
	test('庚申戊寅壬子甲辰','男','XuK01BOOK-P230-食制太过贫贱',(2100,1,1,0,0),(2100,1,1,0,0))
	test('己未己巳丁未辛丑','男','XuK01BOOK-P231-身弱食重发贵',(2100,1,1,0,0),(2100,1,1,0,0))
	test('乙巳乙酉癸酉乙卯','男','XuK01BOOK-P231-干食地印',(2100,1,1,0,0),(2100,1,1,0,0))
	test('丙戌庚寅壬戌甲辰','男','XuK01BOOK-P232-财枭并透食用',(2100,1,1,0,0),(2100,1,1,0,0))
	test('乙未甲申壬寅甲辰','男','XuK01BOOK-P232-枭食相战哀伤',(2100,1,1,0,0),(2100,1,1,0,0))
	test('丁未丁未己亥丁卯','男','XuK01BOOK-P232-偏印同心克尽',(2100,1,1,0,0),(2100,1,1,0,0))
	test('甲戌丙寅甲戌壬申','男','XuK01BOOK-P233-身食俱旺死命',(2100,1,1,0,0),(2100,1,1,0,0))
	test('癸酉乙卯壬辰庚子','男','XuK01BOOK-P237-身旺无依贫夭',(2100,1,1,0,0),(2100,1,1,0,0))
	test('丁未丁未丙午甲午','男','XuK01BOOK-P238-伤尽身旺无依',(2100,1,1,0,0),(2100,1,1,0,0))
	test('甲午丙寅乙未丙戌','男','XuK01BOOK-P239-伤官为忌大凶',(2100,1,1,0,0),(2100,1,1,0,0))
	test('戊辰庚申丁酉壬寅','女','Ye~BOOK-C2-S1-E3',(2100,1,1,0,0),(2100,1,1,0,0))
	test('丙午庚寅庚寅丁亥','男','Ye~BOOK-C2-S2-E3',(2100,1,1,0,0),(2100,1,1,0,0))
	test('壬申癸丑甲辰丁卯','男','Ye~BOOK-C2-S3-E3',(2100,1,1,0,0),(2100,1,1,0,0))
	test('己酉丁丑壬寅辛亥','男','Ye~BOOK-C2-S4-E3',(2100,1,1,0,0),(2100,1,1,0,0))
	test('甲寅辛未戊辰甲寅','男','Ye~BOOK-C3-S1-E1',(2100,1,1,0,0),(2100,1,1,0,0))
	test('丙午甲午壬子辛亥','女','Ye~BOOK-C3-S2-E1',(2100,1,1,0,0),(2100,1,1,0,0))
	test('戊戌己未壬戌丁未','男','YuY16UrlWeixin-从杀格',(2100,1,1,0,0),(2100,1,1,0,0))
	test('庚辰己丑壬戌壬寅','男','ZhangSJ~BOOK-C10-S2-P225',(2100,1,1,0,0),(2100,1,1,0,0))
	test('己卯丁卯丙申甲午','男','Celebrity-Einstein',(1879,3,14,11,30),(1879,4,6,6,21))
	test('癸巳甲子丁酉甲辰','男','Celebrity-毛泽东',(1893,12,26,8,0),(1893,12,7,4,16))
	test('丁未丙午甲午己巳','男','YuY16UrlWeixin-从儿格',(1907,6,14,9,30),(1907,6,7,5,33))
	test('戊申甲子癸亥壬子','男','Celebrity-海灯法师师弟',(1909,1,3,0,30),(1909,1,6,6,45))
	test('丁巳丙午壬午乙巳','男','YuY16UrlWeixin-从财格',(1917,6,9,9,30),(1917,6,6,15,23))
	test('丁巳辛亥丙子壬辰','女','ShaoWH93BOOK-C21-S3-E3',(1917,11,30,8,0),(1917,12,7,0,1))
	test('壬戌己酉壬寅甲辰','男','Celebrity-杨振宁',(1922,10,1,8,0),(1922,10,9,9,41))
	test('庚辰壬午辛亥庚寅','女','外婆',(1940,7,7,4,30),(1940,7,7,15,8))
	test('辛巳辛丑辛酉壬辰','男','Celebrity-Hawking',(1942,1,8,8,0),(1942,1,6,7,2))	
	test('癸未庚申壬戌乙巳','女','ShaoWH93BOOK-C15-S3-E1',(1943,9,1,9,30),(1943,9,8,20,56))
	test('丙戌庚寅丙子癸巳','男','ShaoWH16ESSAY-35',(1946,3,3,9,30),(1946,3,6,12,25))
	test('丙戌甲午己未壬申','男','Celebrity-特朗普',(1946,6,14,15,37),(1946,7,8,2,10))
	test('己丑癸酉甲子壬申','男','1949-10-01-15-中国',(1949,10,1,15,30),(1949,9,8,7,55))
	test('甲午甲戌癸丑甲寅','男','Celebrity-王健林',(1954,10,23,4,0),(1954,11,8,6,51))
	test('辛丑戊戌戊子丁巳','男','我爸',(1961,10,22,9,30),(1961,10,8,20,51))
	test('壬寅癸丑丙辰己亥','女','ShaoWH16ESSAY-62',(1963,1,13,21,30),(1963,1,6,9,27))
	test('癸卯丁巳庚辰壬午','女','雁青妈',(1963,6,6,12,0),(1963,6,6,18,14))
	test('甲辰甲戌丁酉戊申','男','Celebrity-马云',(1964,10,15,16,0),(1964,11,7,17,15))
	test('丙午庚寅丙申己丑','男','雁青爸',(1966,2,6,2,0),(1966,3,6,8,52))
	test('戊申癸亥辛卯丁酉','男','Celebrity-李彦宏',(1968,11,17,17,26),(1968,12,7,9,9))
	test('戊申癸亥己酉壬申','女','Celebrity-邓文迪',(1968,12,5,16,30),(1968,11,7,16,30))
	test('己酉戊辰甲戌辛子','女','我妈',(1969,4,29,0,0),(1969,5,6,0,50))
	test('辛亥丙申己丑戊辰','男','YuY17UrlWeixin-0311-清华本科',(1971,9,1,8,31),(1971,8,8,12,40))
	test('辛亥戊戌丁亥甲辰','男','Celebrity-马化腾',(1971,10,29,8,0),(1971,10,9,6,59))
	test('甲寅壬申癸巳壬子','男','云明朋友',(1974,8,20,0,0),(1974,9,8,8,45))
	test('乙卯癸未甲子乙亥','男','Celebrity-陶哲轩',(1975,7,17,21,30),(1975,7,8,1,59))
	test('乙卯丙戌乙巳丁丑','男','2017-02-18-23-武汉事件老板',(1975,10,26,2,0),(1975,10,9,6,2))
	test('丙辰戊戌乙巳辛子','男','骆康福',(1976,10,20,0,0),(1976,11,7,14,59))
	test('丁巳己酉辛未壬辰','女','Celebrity-谭晶',(1977,9,11,8,30),(1977,10,8,17,44))
	test('丁巳壬子辛亥己亥','女','TBCP24-dq771228',(1977,12,20,22,57),(1978,1,6,0,44))
	test('己未戊辰辛未庚寅','男','TBCP12-乔峰老大406',(1979,5,4,4,4),(1979,4,5,17,18))
	test('庚申乙酉癸卯壬戌','男','ZZZ15UrlSina-E1',(1980,9,27,20,0),(1980,10,8,11,20))
	test('辛酉丁酉己未戊辰','男','QQCP17-Mosquiton',(1981,10,8,8,45),(1981,9,8,1,43))
	test('壬戌庚戌庚寅庚辰','男','TBCP23-80010086',(1982,11,3,7,37),(1982,11,8,2,4))
	test('癸亥辛酉乙丑戊寅','女','ZZZ15UrlSina-E2',(1983,10,4,4,0),(1983,10,9,4,51))
	test('癸亥乙丑癸丑丙辰','女','马云明',(1984,1,20,8,0),(1984,1,6,11,41))
	test('甲子丙寅丁酉乙巳','女','ZZZ16UrlSohu-自刑',(1984,3,4,9,30),(1984,2,4,23,19))
	test('甲子丁卯戊申辛酉','女','Buddhist-西安19840315',(1984,3,15,17,30),(1984,3,5,17,25))
	test('甲子丁卯壬子己酉','女','Buddhist-西安19840319',(1984,3,19,17,30),(1984,3,5,17,25))
	test('甲子甲戌辛丑戊戌','男','QQCP1-474422585',(1984,11,3,19,30),(1984,11,7,13,46))
	test('甲子乙亥庚申辛巳','男','TBCP1-洪武男',(1984,11,22,10,30),(1984,12,7,6,28))
	test('甲子庚午壬申甲辰','男','云明案例1',(1984,12,1,0,0),(1984,12,8,0,0))
	test('乙丑庚辰戊子丁巳','男','SGCP2-vampire',(1985,4,19,10,45),(1985,4,5,4,14))
	test('乙丑壬午辛卯甲午','男','QQCP2-396545090',(1985,6,21,12,37),(1985,6,6,2,0))
	test('乙丑甲申丙申癸巳','女','QQCP18-红杉树',(1985,8,25,10,30),(1985,9,8,0,53))
	test('乙丑乙酉辛亥戊子','男','郭凯莹老公',(1985,9,9,0,0),(1985,9,8,0,53))
	test('乙丑戊子乙巳辛巳','女','云明朋友',(1986,1,1,10,0),(1986,1,5,23,28))
	test('丙寅癸巳甲戌乙亥','女','QQCP20-为爱拼搏',(1986,5,30,21,0),(1986,5,6,3,31))
	test('丙寅甲午庚寅丙戌','女','QQCP3-106931345',(1986,6,15,19,30),(1986,6,6,7,44))
	test('丙寅己亥壬戌壬寅','男','Clergy-福建1986',(1986,11,14,3,30),(1986,12,7,18,1))
	test('丁卯甲辰壬寅庚戌','女','青哥老婆',(1987,5,20,19,30),(1987,5,6,9,6))
	test('丁卯己巳戊申丙辰','女','TBCP25-硒酸',(1987,6,28,7,45),(1987,7,7,23,39))
	test('丁卯戊申戊戌丁巳','男','黄伟',(1987,8,17,10,50),(1987,8,8,9,29))
	test('丁卯庚戌己亥丁卯','女','DBCP1-Snail',(1987,10,17,6,0),(1987,11,8,7,6))
	test('丁卯壬子丁巳庚子','男','Celebrity-王思聪',(1988,1,3,0,0),(1987,12,7,23,53))
	test('戊辰丙辰戊戌乙卯','男','黄波',(1988,4,13,6,30),(1988, 5,5,15,2))
	test('戊辰丙辰辛亥癸巳','男','海南省建府',(1988,4,26,10,24),(1988, 5,5,15,2))
	test('戊辰辛酉甲戌丁卯','女','TBCP2-圣心若水',(1988,9,16,5,30),(1988,9,7,18,12))
	test('戊辰癸亥丁丑辛丑','男','杨圣行',(1988,11,18,2,0),(1988,12,7,5,35))
	test('戊辰癸亥乙酉丙子','男','SGCP1-乜禄',(1988,11,26,0,30),(1988,12,7,5,35))
	test('戊辰癸亥壬辰辛亥','男','QQCP4-873624929',(1988,12,3,21,30),(1988,12,7,5,35))
	test('戊辰甲子丙辰戊子','男','TBCP20-乙未还是丙申-清华',(1988,12,27,0,37),(1989,1,5,16,46))
	test('己巳丙寅丁未甲辰','男','QQCP6-316965678',(1989,2,16,7,30),(1989,2,4,4,27))
	test('己巳丁卯辛巳丁酉','男','王成富',(1989,3,22,17,00),(1989,3,5,22,34))
	test('己巳戊辰丁巳丙午','男','TBCP17-usdotaer',(1989,4,27,11,30),(1989,4,5,3,39))
	test('己巳庚午辛酉丁酉','男','黄平',(1989,6,30,18,30),(1989,6,6,1,5))
	test('己巳癸酉乙未丙子','男','TBCP16-再见大萝卜',(1989,10,1,23,30),(1989,9,7,0,25))
	test('己巳甲戌辛酉甲午','女','羽衣同学一',(1989,10,28,12,10),(1989,11,7,18,34))
	test('己巳乙亥甲午甲子','女','郭凯莹',(1989,11,30,0,0),(1989,12,7,11,20))
	test('己巳丙子己酉壬申','男','TBCP11-这世界怎么了OK',(1989,12,15,15,35),(1989,12,7,11,21))
	test('庚午戊寅丙午乙未','女','TBCP21-hua_0210',(1990,2,10,14,0),(1990,2,4,10,14))
	test('庚午己卯己丑丙寅','女','王云华',(1990,3,25,4,0),(1990,3,6,4,20))
	test('庚午庚辰壬子庚戌','女','李雁青',(1990,4,17,20,55),(1990,4,5,9,13))
	test('庚午癸未癸卯癸丑','女','张楠',(1990,8,6,2,30),(1990,7,7,17,1))
	test('庚午乙酉戊寅癸亥','男','刘磊',(1990,9,10,22,30),(1990,10,8,21,14))
	test('庚午丁亥丁丑庚戌','女','王晓彤',(1990,11,8,20,0),(1990,11,8,0,24))
	test('庚午丁亥丁亥辛丑','男','QQCP8-怪兽',(1990,11,18,2,30),(1990,12,7,17,15))
	test('庚午戊子壬戌辛亥','男','黄阳焕',(1990,12,23,21,30),(1991,1,6,4,28))
	test('庚午己丑丙申癸巳','女','曾纪璇',(1991,1,26,10,30),(1991,1,6,4,28))
	test('辛未庚寅癸亥己未','女','庞艳春',(1991,2,22,14,30),(1991,3,6,10,12))
	test('辛未辛卯丁丑丁未','男','TBCP15-粉底留香',(1991,3,8,16,25),(1991,3,6,10,12))
	test('辛未辛卯甲午辛未','男','刘龙',(1991,3,25,14,3),(1991,3,6,10,12))
	test('辛未己亥庚子丙子','男','夏高峰',(1991,11,26,0,30),(1991,11,8,6,8))
	test('壬申乙巳乙酉戊寅','男','QQCP7-1219938700',(1992,5,9,4,30),(1992,6,5,18,22))
	test('壬申乙巳甲辰庚午','男','2017-02-23-13-加拿大留学生绑匪张天一',(1992,5,28,11,30),(1992,6,5,18,22))
	test('壬申丁未乙酉己卯','男','李述洋',(1992,7,8,6,30),(1992,8,7,14,28))
	test('壬申戊申乙丑庚辰','女','TBCP4-蔷薇呼救信号',(1992,8,17,8,10),(1992,8,7,14,28))
	test('壬申己酉癸卯己未','女','TBCP17-Bettle呼哈',(1992,9,24,14,0),(1992,9,7,17,19))
	test('壬申庚戌己巳丙寅','女','QQCP-天道阳回',(1992,10,20,4,0),(1992,10,8,8,52))
	test('壬申辛亥戊子壬戌','男','李彦杰2018年男友',(1992,11,8,20,10),(1992,12,7,4,45))
	test('壬申辛亥庚戌壬午','女','QQCP9-574386751',(1992,11,30,11,30),(1992,11,7,11,57))
	test('癸酉丙辰癸亥壬子','男','张崇',(1993,4,12,0,0),(1993,4,5,2,37))
	test('癸酉丙辰甲戌丁卯','男','QQCP10-何朝田',(1993,4,23,6,0),(1993,4,5,2,37))
	test('癸酉丁巳庚子壬午','男','QQCP11-892556013',(1993,5,19,11,30),(1993,5,5,20,2))
#	test('癸酉戊午戊辰己未','女','TBCP3-═',(1993,6,16,13,30),(1993,7,7,10,32))
	test('癸酉戊午甲戌庚午','女','QQCP12-623606879',(1993,6,22,11,30),(1993,7,7,10,32))
	test('癸酉戊午丁丑庚子','男','TBCP16-不带一丝杂质',(1993,6,24,23,11),(1993,6,6,0,15))
	test('癸酉庚申戊寅辛酉','男','陈奕达',(1993,8,25,18,30),(1993,8,7,20,18))
	test('癸酉壬戌乙丑庚辰','男','QQCP15-李佳鑫',(1993,10,11,8,0),(1993,10,8,14,40))
	test('癸酉癸亥戊申癸丑','女','黄碧霞',(1993,11,23,2,30),(1993,12,7,10,34))
	test('癸酉甲子辛巳甲午','男','TBCP18-Bettle呼哈男友',(1993,12,26,11,0),(1993,12,7,10,34))
	test('甲戌戊辰己巳甲子','男','TBCP10-爪狸',(1994,4,13,0,8),(1994,5,6,1,54))
	test('甲戌己巳庚子丙子','女','TBCP19-婉依紫陌',(1994,5,13,23,40),(1994,5,6,1,54))
	test('甲戌己巳庚戌丙子','男','迪玛希',(1994,5,24,0,0),(1994,6,6,6,5))
	test('甲戌壬申丙子庚寅','男','三舅儿小柱',(1994,8,18,4,50),(1994,9,8,4,55))
	test('乙亥甲申甲午丙寅','男','QQCP19-山寨小车胎',(1995,8,31,4,37),(1995,8,8,7,52))
	test('甲戌癸酉癸卯乙卯','男','2017-02-18-23-武汉事件凶手',(1994,9,14,5,30),(1994,10,8,20,29))
	test('乙亥丁亥庚午丙戌','女','李杨',(1995,12,5,19,30),(1995,12,5,22,23))
	test('乙亥丁亥丙寅壬辰','男','QQCP16-纯粹',(1995,12,1,7,57),(1995,11,8,5,36))
	test('乙亥戊子癸巳庚申','女','李雁杰',(1995,12,28,16,0),(1996,1,6,9,31))
	test('丙子己亥丙寅癸巳','女','TBCP13-做人不听狗日龙',(1996,11,25,10,30),(1996,11,7,11,27))
	test('丁丑壬寅乙未辛巳','男','QQCP22-1214627836',(1997,2,22,10,0),(1997,2,4,3,2))
	test('丁丑甲辰庚寅庚辰','男','李占胜',(1997,4,18,8,0),(1997,4,5,1,56))
	test('丁丑乙巳壬子戊申','女','TBCP8-再回首与who',(1997,5,10,16,14),(1997,6,5,23,33))
	test('丁丑乙巳甲子乙亥','女','TBCP22-伍婷华',(1997,5,22,21,30),(1997,6,5,23,33))
	test('戊寅丙辰壬寅辛亥','女','TBCP14-然公子的猫',(1998,4,25,21,5),(1998,4,5,8,6))
	test('戊寅辛酉甲子壬申','男','QQCP21-刘政',(1998,9,14,16,10),(1998,10,8,19,56))
	test('戊寅己未戊寅甲寅','男','ZZZ15Url-飞财',(1998,7,30,3,30),(1998,8,8,1,20))
	test('戊寅庚申戊子戊午','女','TBCP5-卿远annn',(1998,8,9,12,0),(1998,8,8,1,20))
	test('戊寅辛酉戊辰乙卯','男','QQCP5-九思',(1998,9,18,5,40),(1998,10,8,19,56))
	test('戊寅壬戌辛丑丁酉','女','QQCP13-397857838',(1998,10,21,18,30),(1998,10,8,19,56))
	test('己卯壬申庚子己卯','女','TBCP7-Sfhhhghhu',(1999,8,16,6,0),(1999,9,8,10,10))
	test('庚辰己卯辛未辛卯','男','QQCP14-943023949',(2000,3,14,5,0),(2000,4,4,19,32))
	test('甲申丙子辛酉壬辰','男','TBCP9-zhu819051239',(2004,12,8,7,30),(2005,1,5,14,3))
	test('丁亥壬寅庚辰辛子','男','骆凯铭',(2007,2,15,0,0),(2007,2,4,13,14))
	test('丁亥辛亥丁卯辛子','女','骆慧',(2007,11,29,0,0),(2007,12,7,20,12))#	
	test('癸巳戊午庚申辛子','女','骆嘉萌',(2013,6,23,0,0),(2013,7,7,7,9))
	test('癸巳己未己丑壬申','男','Celebrity-剑桥王子',(2013,7,22,16,30),(2013,7,7,7,9))	
	test('癸巳甲子辛亥癸巳','女','青哥老婆大女',(2013,12,11,10,0),(2014,1,5,20,7))
	test('甲午己巳乙巳壬午','男','黄子航',(2014,6,3,11,30),(2014,6,6,2,3))
	test('丙申丁酉辛丑庚寅','女','青哥老婆小女',(2016,9,16,4,30),(2016,9,7,13,48))
	test('丙申庚子丁亥戊申','女','TBCP6-w311312',(2016,12,31,15,30),(2016,12,7,0,41))
	test('丙申辛丑甲辰丁卯','男','Celebrity-黄晓明儿子',(2017,1,17,6,0),(2017,2,3,23,35))
	test('丁酉乙巳甲寅戊辰','男','Celebrity-黄磊儿子',(2017,5,27,8,35),(2017,5,5,15,32))
	test('丁酉己酉己酉辛未','男','包艳萌儿子',(2017,9,19,13,30),(2017,9,7,18,39))
#	test('丁酉丙午庚午','男','鸿宝',(2017,6,20,0,0),(2017,6,8,0,0))
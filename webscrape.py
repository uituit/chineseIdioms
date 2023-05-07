# import the libraries
import requests
import pandas as pd
from bs4 import BeautifulSoup

def book_check(element):
    if element.find_all('font'):
        return "False"
    else:
        return "True"
    
allCharacters = '一乙丁七乃乜九了二人入八几刀刁力匕十卜又丈三上下丫丸久么乞也于亡兀凡刃勺千叉口土士夕大女子孑寸小尸山川工己已巳巾干幺弋弓才不丐丑中丰丹之予云互五井亢什仁仃仄仆仇今介仍允元內公六兮冗凶分切刈勻勾勿化匹升午卞卬厄及友反壬天太夫夭孔少尤尹尺屯巴巿幻弔引心必戈戶手扎支文斗斤方无日曰月木欠止歹殳毋比毛氏水火爪父片牙牛犬王且丕世丘丙丱主乍乎乏仕他仗付仙仞仟仡代令以仨兄充冉冊冬凸凹出刊功加包匆北匝卉半占卮卯去古句另叨叩只叫召叮可台叱史右叵司囚四外央夯失奴奶孕它宄尻左巧巨市布平幼庀弁弗弘忉扒打扔斥旦未末本札正母民永氾汀汁犯玄玉瓜瓦甘生用甩田由甲申疋白皮目矛矢石示禾穴立丞丟亙交亥亦仰仲仳件任份仿企伈伉伊伍伎伏伐休伔兆兇先光全共再冰冱刎刑刓刖列劣匈匠匡印危吁吃各吆合吉吊同名后吏吐向吒吓吖回因在圪圬圭圮地夙多夷夸奸好妁如妃妄字存宅宇守安寺尖屹屺州帆年式弛忖忘戌戍戎成托扛扞扢扣收旨早旬旭曲曳有朱朵朽朿次此死汍汕汗汙汜汝江池污灰牝牟犴百竹米缶羊羽老考而耒耳聿肉肋肌肍臣自至臼舌舛舟色芋血行衣西邙阡串些亨伯估伴伶伸伺似但佇佈位低住佐佑佔何佗余佚佛作佞你克兌兵冶冷刜初判別刦刨利刪助努劫劬劭匣卲即卵厎君吝吞吟吠否吪含听吭吮吳吵吶吷吸吹吻吼吾呀呂呆呈告呐囤囫囮困址坂均坊坌坍坎坐坑块壯夾妒妓妖妙妝妣妥妨孚孜孝宋完宍宏尨尪尬尾尿局屁岌岐岑岔巡巫希庋序延廷弄弟形彤彷役忌忍忐忑忒志忙忝忠忡忤忨忪快忭忮忱忲忳忷忸忺忻忼我戒扭扮扯扱扳扶批扺扼找技抂抃抄抉把抑抒抓抔投抖抗折抛攸改攻旰旱更杅杆杉杌李杏材村杓杕杖杜杞束杠步每求汞汩汪汰汲汴汶汹決汾沁沂沃沄沅沆沈沉沌沐沒沖沙沛灶灸灺灼災牡牢狂狃狄玘甫男甸町疔皁皂矣祀禿秀私究系纳纾肓肖肘肚肝良芒見角言谷豆豕豸貝赤走足身車辛辰迂迄迅邑邢那邦邪酉里阨阪阫阬阮阱防㓟並乖乳事亞亟享京佩佪佯佰佳併佶佹佻佼使侁侃侄來侈例侍侏侔侖侘侚供侜依免兒兔兕兩其具典冽函刮到刳制刷券刺刻剁劻劾匼卑卒卓協卦卷卸厓叔取受呢周呫呰呱呲味呴呵呶呷呻呼命呾呿咀咂咄咆咈咋和咍咎咒咕囷囹固坡坤坦坯坰坱坷坼垂夜奄奇奈奉妹妻妾姊始姍姐姑姓委孟季孤孥宕宗官宙定宛宜尚屄居屆屈岡岫岱岳岵岸帑帔帕帖帙帚帛并幸底庖店庚府弢弦弧弩彼往征徂念忽忿怊怍怏怔怕怙怛怡怦性怩怪怫怯怳怵戔戕或戾房所承披抬抱抵抶抹抻押抽拂拄拆拇拈拉拊拋拌拍拐拑拒拓拔拖拗拘拙拚招放政斧斨於旺旻昂昃昆昇昊昌明昏易昔朋服杭杯杰東杳杵杷杼松板枇枉枋枌析枕林枘枚果枝欣武歧歿毒氓氛沓沫沬沮沱河沸油治沽沾沿泀況泄泅泆泊泌泐泓法泗泛泡波泣泥注泫泮泯泱泳炊炎炒炙爬爭牀版牧物狀狉狎狐狗玠玢玦玩甿畀疙疚的盂盱盲直知矻社祁秉穹空糾绌罔罕羌者股肢肥肩肫肬肮肯肱育肴肹肺臥臾舍艾芬芳虎虯虱軋迍迎近迓返邯邱邵邸采金長門阜阸阻阽阿陀陂附雨青非亭亮侮侯侵侶便係促俄俊俎俏俐俑俔俗俘俚俛俜保俞俟俠信兹冑冒冠則剉削剋剌前剎勁勃勇勉匍匽南卻卼厖厚叛咤咥咧咨咫咬咮咳咶咷咸咻咽咿哀品哂哄哆哇哈哉囿型垓垛垠垢垣垮城奏奐契奓奔奕妍姚姜姝姞姣姥姦姨姮姱姹姻姿娀威娃孩客宣室宥宦封屋屍屎屏峋峙巷巹帝帡帢帣帥幽庥度建廻弇弈弭弮彥待徇很徉徊律後怒思怠急怨恂恃恆恇恍恑恛恟恢恤恨恪恫恬恰扁扃拏拜括拭拯拱拷拼拽拾持挂指按挎挑挖故斫施既星映春昧昨昭是昵曷朐枯枳枵架枷枹枻枿柁柄柏柑染柔柙柚柜柝柢查柬柯柱柳柴柵歪殃殄殆段毖毗泉泚洇洊洋洌洏洗洛洞洟津洩洪洫洲洵洶洸洹活洽派洿流炧炫炬炭炮炯炰炳炷炸為爰牯牲狟狠狡狥狧狩玲玷珂珉珊珍甚畋界畎畏疢疣疤疥疫癸皆皇皈盃盆盈相盹盻盼盾省眄眇眈眉眊看矜矧砂砉砌砍砑祆祇祈祌祝禹秋科秒秕穿突竽竿紀紂約紅紆紇紈紉给缸美羿耇耍耐耶耷胃胄背胎胏胖胙胛胝胞胠胡胤胥致芊芍苗苞英范虐虹虺虻衍衎表衫要觔訂計貞負赳赴軌軍迢迤迥迨迪迫迭述郄郊郎酊重閂陋陌降限面革韋韭音風飛食首香乘修俯俱俶俸俾倀倆倉個倍倏倒倔倕倖倘候倚倜借倡倥倦倨倩倪倫倳倸值兼冓冢冤冥凄凊凋凌凍剔剖剗剚剛剜剝剡匪厝原叟員哥哨哪哭哮哲哺哼哽唅唆唇唉唏唐唧圃圄埃埋埏埒夏套奚姬娉娑娓娖娘娛娜娟娥娩娭孫宮宰害宴宵家容射屐屑展峨峭峰峴島峻峽差帨師席座庫庬庭弱徐徑徒恐恕恙恝恣恥恩恭息悂悃悄悅悌悍悒悔悖悚悛悞悟扅扆扇拳拿挈挐挨挪挫振挹挺挼挽挾捂捃捆捉捋捍捎捏捐捕效料旁旂旃旄旅旆時晃晉晌晏書朒朔朕栗校栩株栲核根格栽桀桁桂桃框案桉桊桌桐桑桓桕欬欱殉殊殷氣氤泰浚浡浦浩浪浮浴海浸浹浼涅涇消涉涌涎涓涕涘烈烏烘烙烜烝烟特狶狷狸狹狼狽珠珥珩珪班珮琉瓞瓟瓴畔留畛畜畝疲疵疼疽疾疿痀痂病症皋益盍盎眐眙眚眛真眠眢眥眦眨眩矩砠砢砣砥砭砰破砸祓祕祖祗祚祛祜神祟祠秘租秣秤秦秩积窄窆窈站竛笆笇笈笏笑粉紊紋納紓純紕紗紘紙級紛紜素索缺罡羔翁翅耄耆耕耗耘耙耻耽耿胭胯胸胹胼能脂脅脆脈脊臬臭舐航般芙芝芟芥芰花芷芸芹芻芽芾茫茲茸荊虔蚊蚋蚌蚍蚑蚓蚘蚤蚩蚪衄衰衲衷衹衽衾衿袁袂袄訊討訐訓訕訖託記豈豹豺財貢貤起躬軏軒軔辱迴迷迹追退送逃逅逆通邕郡郢郤酌配酒釘釜針閃陝陟陡院陣除陧隻隼馬骨高鬥鬯鬲鬼乾偃假偈偉偎偏偕偘做停偢健偪偭偲側偶偷偽兜冕凰剪剮副勒動勖勘務匏匐匙匾匿區卿參叄唬售唯唱唲唳唶唸唾啄商問啐啕啖啜啞啟圇圈圉國域埠埤埴埶執培基埽堀堂堅堆堊娶娼婀婁婆婉婑婗婚婢婦婪孰宿寂寄寅密寇將專尉屙屜崇崎崑崔崖崗崙崚崟崢崦崧崩巢帳帶帷常庳庵庶康庸張強弸彗彩彪彫彬得徘徙徜從徠悉悠患悤悰悱悴悵悸悼悽情惆惇惋惏惓惔惕惘惙惚惛惜惝惟戚戛扈挲捥捧捨捩捫捭捰捱捲捶捷捺捻捽掀掂掃掄掇授掉掊掎掏掐排掖掘掙掛掞掠採探掤接控推掩措掬敏救敕敖敗敘教斌斛斜斬旋旌旍旎族晚晝晞晤晦晨曹曼朗朘望桮桴桶桷桿梁梂梅梓梗條梟梢梧梨梭梯械梲梳梵欲欷殍殺毫涫涯液涴涵涷涸涼涿淄淅淆淈淋淌淑淒淘淚淜淡淤淥淨淪淫淬淮深淳淵混淹淺添清渚烱烹烺烽焉爽牽牾犁猊猖猗猙猛猜猝率現球琅理瓠瓶甜產畢畤略畦異痌痍痏痔痕皎盒盔眯眴眵眶眷眸眹眺眼眾着研硃硎祥祧票祭移窒窕竟章笙笛笞笠笤笥符笨笫第笯笵粒粕粗粘紮累細紱紲紳紵紹紿絀終組絆绪缽罣羚羝羞習耈耜聆聊胔脖脛脝脣脩脫脬脯脰脱舂舳舵舸船艴苑苒苔苕苛苜苟苡若苦苫苴苶苻茁茂茄茅茆莉莊莎莫華處蚰蚶蛀蛆蛇蛉蛋衒術袋袍袒袓袖袗袞袨袪被覂規覓視訛訟訣訥訩訪設許豉豚貧貨販貪貫責赦趾跂軛軟逋逌逍透逐逑途逕逖逗這逛逝逞速造逡逢連部郭郵酕酖野釣釧釵閉陪陬陰陳陵陶陷陸雀雩雪頂頃飡飢飣馗魚鳥鹵鹿麥麻傀傅傍傑傖傘備傜凱剩割創勛勝勞博厥啻啼啾喁喂喃善喇喉喊喋喏喑喔喘喙喚喜喝喟喣喧喪喬單喳喻圍堙堠堤堪堯堰報場堵堿壹壺奠奡奢奥婷婺婿媒媕媚媟媠媮嫏孱富寐寒寓寔尊尋就屠嵁嵇嵌嵎嵐巽帽幀幃幄幅幾庾廁廂廊弼彘彭御徨復循悲悶惄惑惠惡惰惱惲惴惶惸惺惻愀愉愊愎愒愔愕愜愣慨戟扉扊掌掣掰掿揀揄揆揉揎描提插揖揚換揜揠握揣揪揭揮援揵揶揸攲敝敞敢散敦斐斑斝斯晬普景晰晴晶晷智晻晼暑曾替最朝期棄棉棋棍棐棒棖棗棘棚棟棠棣棧棨棬森棰棱棲棹棺棼植椎椒椓欹欺欽款欿殖殘殼殽毳淼渙減渝渟渠渡渣渤渥渦渫測渭港渰渲渴游渺渻渾湃湄湊湍湎湔湖湘湛湜湧湫湮湯湲溈溉滋焚焜無焦焮焯焰然煮牌犀犄猒猢猥猱猲猴猶猷琚琛琢琦琨琪琬琯琰琱琳琴琵琶瓻甥甯番畫畯疎疏痗痛痞痡痣登發皓皴盛盜睃睍短硜硝硬硯硶祲稀稂稅稈稊程稍税窖窗窘竣童竦笄筆等筋筌筍筏筐答策粟粢粥粧紫結絓絕絜絝絞絡絢絣給絫絮絰統絲絳缾羡翔翕耋聒脹脾腆腋腎腑腔腕舃舄舒舜茗茞茨茵茶茹荀荃荄草荏荑荒莽菽虛虜蛔蛘蛙蛛蛟蛣蛤蛩街袱袴袵袷裀裁裂裉覃觚訴訶註訾詀詁詆詈詎詐詒詔評詖詘詞詠象貂貯貰貲貳貴貶買貸費貼貽貿賀賁赧趁趄超越跅跇跋跌跎跑跖跗跚跛距軫軸軺軼辜迸逮週進逴逵逶逸都鄂鄉酡酢酣酤酥量鈇鈍鈐鈔鈞開閎閏閑閒間閔陽隃隅隆隈隉隊隋階雁雄雅集雇雈雲韌項順頇須飥飦飧飨馭馮馱黃黍黑亂傫催傭傯傲傳傴債傷傺傻傾僂僄僅僇僉剸剽剿募勠勢勤匯嗅嗇嗉嗐嗑嗒嗓嗔嗙嗚嗛嗜嗟嗡嗣嗤嗥園圓塊塌塑塔塗塘塚塞塢塤填奧媲媳媸媺媼媽嫁嫂嫉嫌孳寖寘尠嵩嵫嵬嵲幌幹廈廉廋彀徭微徯想惹愁愆愈愍意愚愛感愧愴愷愾慄慆慊慌慍慎戡戢揫搆損搏搓搔搖搗搘搜搞搠搡搢搤搥搦搧搨搪搬搭搰搶搽敬斟新旒暄暇暈暉暍暖暗暘會椽椿楊楓楔楗楚楛楞楣楫業楮楯極楶楷楹楺概榆歃歇歲殛殿毀毁毓毷源溓準溘溜溝溟溢溥溪溫溯溲溶溷溺溽滂滄滅滉滑滓滔漓煉煊煌煎煖煙煞煢煤煥煦照煨煩煬爺牒猻猾猿獅瑀瑋瑑瑕瑚瑜瑞瑟瓿當畸畹痰痹痺痼痾痿瘁皙盞盟睒睖睚睛睜睞睟睡睢督睥睦睨睩睫睬矮碌碎碑碓碗祺祻祿禁禽稔稗稚稛稜稟稠窟窠筠筭筮筲筵節粱粲粵絛絹絺絿綁綃綆綈綏經罨罩罪置署群羨義翛聖聘肄肅肆腥腦腧腫腭腮腯腰腳腴腸腹腼舅荷荻荼莒莖莘莛莞莠莩莪萬董蒂虞號蛺蛻蛾蜀蜂蜃蜇蜉蜊蜎蜑蜒蜓衙裊裋裎裏裒裔裕裘裙補裝觜解觥詡詢詣試詩詫詬詭詮詰話該詳詵詹詼誅誆誇豢貅貉貊賂賃賄賅資賈賊趑趒趼跟跡跣跤跧跨跪跫跬路跱跳跺躲軾較輅輇輈載輊辟農逼逾遁遂遄遇遊運遍過遏遐遑遒道達違鄒酩酬鈴鈿鉅鉈鉉鉏鉗鉚鉛鉞鉤鉥鉦閘隔隕隗隘隙雉雋雌雍雎零雷雹電靖靳靴靶頌預頑頓飩飫飭飯飱飲馳馴骫髡鳧鳩麂黽鼎鼓鼠像僕僚僝僢僥僦僧僨僪僬僭僮僰兢凳劃劄匱厭嗷嗼嗽嘁嘆嘈嘉嘎嘏嘐嘑嘔嘖嘗噓圖團塵塹墁境墉墊墐墓壽夢夤夥奪嫖嫗嫚嫛嫠嫡嫣嫦嫩嫫寞察寡寢寤寥實寧寨對屢屣嶂嶄嶇幕幗廓廕彰愬慈態慘慚慞慟慢慣慳慵慶慷截搴摋摐摑摔摘摛摜摟摧摭摳摶摸摽撂敲斠斡斲旖旗暝暢暨榖榛榜榦榨榫榭榮榱榴榷榻榼槁槃槊構槌槍槎槐槓歉歌殞氳滌滚滫滯滲滴滾滿漁漂漆漏演漕漚漠漢漣漫漬漭漱漲漳漶漸漾煽熄熊熏熒熔熙爾犒犖獄獍獎獐瑣瑤瑯瑰瑱瑳甄畽疐疑瘋瘌瘏瘕瘖皸盡監睹睽睿瞅碟碣碧碩碫碬碰碴禍禎福種稱窩窪窬竭端箇箋箍箎箏箐箑箔箕算箝管粹粼精綜綠綢綣綦綫綬維綮綰綱網綳綴綵綸綺綻綽綾綿緇緊緋緌緒罰翠翡聚聞肇腐腿膀膂膇膈膊膏臧臺與舔舕舞菀菁菅菊菌菘菜菟菩菰菱菲菹萁萃萇萊萋萌萍萎萑著蒲蒼蒿蓮虡蜚蜜蜣蜩蜮蜯蜻蜾蝂裨裯裳裸裹裼製裾觫認誑誓誕誘誚語誠誡誣誤誥誦誨說説豨豪貌賑賒賓賕赫趕趙跼跽踄踅踆踉踊輒輔輕辣遘遙遜遝遞遠遣鄙鄢酲酷酸酺鉺銀銃銅銓銖銘銜閡閣閤閥閦閨際障隟雒需鞀鞅韶頗領颭颮颯飴飼飽飾駁骯髦髧髩魁魂鳲鳳鳴鳶麼鼻齊僵僶價僻僽僾僿儀儂億儆儈儉儋凜劇劈劉劌劍厲嘩嘮嘯嘲嘴嘵嘶嘹嘻嘿噀噁噂噉噍噎噙噴圚墜增墟墨墩墮墳嫵嫻嬈嬉嬋嬌審寫寬導層履嶒嶔嶙嶠嶢幞幟幡幢幣廚廝廟廡廢廣弊彈彉影徵德徹慕慝慧慮慰慸慾憂憍憎憐憒憔憚憤憧憫憮憰憲戮戱摩摯摹撅撇撈撋撏撐撒撓撕撙撚撝撞撟撤撥撧撩撫播撮撰撲整敵敶敷數敺敻暫暮暱暴槧槳槽槿樀樁樂樊樑樓樕樗標樛樞模樣歎歐殢殣殤毅毆氂滕漿潁潑潔潘潛潠潢潤潦潭潮潰潸潺潼澄澆澇澈澌澍澎澒澗熟熠熨熬熭熯熱熳牖犛獗獠瑩瑾璀璃璆璇璉璋瘙瘝瘞瘟瘠瘡瘢瘤瘥瘦瘧瘩皚皺盤瞇瞋瞍瞎瞑確碻碼磅磈磊磋磐磑磔磕稷稻稼稽稿穀窮窯窳箭箱箴箸箾篁範篆篇篋糅糈糊緗緘線緜緝緞緟締緡緣編緩緬緯緲練緻罵罷羭羯翥翦翩翫翬耦聩膕膘膚膜膝膠萱萼落葄葅葆葉葑葙葛葦葩葫葬葭葳葵葷葸葹葺蔑蔕蔬虢蝌蝍蝎蝓蝕蝘蝜蝟蝠蝣蝥蝦蝮蝴蝶蝸衛衝複褊褌褎褐褒褓褔褕褚覥觭誰課誳誶誷誹誻誼誾調諂諄談諉請諍諏諑諒諕論諸豎賙賜賞賠賡賢賣賤賦質賬趣踏踐踔踕踖踞踟踢踣踧踩踪躺輗輝輟輠輦輩輪遨適遭遮遯鄧鄭鄰鄲醁醄醅醇醉醋銳銷銼鋃鋌鋏鋒鋙鋣鋤鋥鋪閬閭閱霄霆震霈靚靠鞋鞍頞頦餉養餌駐駑駒駕駘駛駝駟骴髫髭髮髯鬧魃魄魅魆魯魴鳷鴃鴆鴇鴉麄麾黎鼐齒㕙㗲儒儔儕儗儛冀凝劑劓勳噞噤噥噦器噩噪噬噯噱噲圜墺墾壁壅壇奮嬙嬛嬴學寰嶮廩廪彊徼憊憋憑憖憝憨憩憶憺憾懂懇懈應懊懌懍懓戰撻撼撾撿擁擂擄擅擇擋操擐擒擔擗據曆曇曉樵樸樹樽橄橅橈橋橐橘橙橛機橡橫橱歔歕歙歷殪殫澠澡澤澥澧澨澭澮澹激濁濃濊熹熾燁燃燈燋燎燒燔燕燙犟獨獪璐璚璜璞璠璣瓢甌甍瘳瘴瘵瘸瘼盥盧瞚瞞瞠瞢磚磢磣磨磬禦穆積穎窺竮竱築篙篚篝篡篤篦篨篩篪糖糗縈縉縋縑縕縗縛縝縞縟縣罹羲翮翰翱耨膨膩膳臲臻興舉蒐蒓蒙蒜蒞蒡蒢蒭蒯蒸蒹蓁蓄蓆蓉蓋蓍蓐蓑蕪螂螃融螓螗螞螟螢衡褞褡褥褦褧褪褫褰褲覦覩親觱諛諝諞諢諤諦諧諫諭諮諱諳諶諷諺諼諾謀謁謂豫豬豭貓賭賴赬赭趦踰踱踴踵踹踽蹀蹁蹄蹅輯輳輶輸輻辦辨遲遵遷選遹遺遼鄴鄶醍醐醑醒鋸鋼錄錐錘錙錚錢錦錫錮錯閶閻閼閽閾隧隨隩險雕霍霎霏霓霖靜靦鞘頤頭頰頷頸頹頻餐餒餓餔餖餗餘駢駭駮駱骸骼髻鬨鮐鮑鮒鮓鴒鴛鴞鴟鴣鴦鴨麇麈黔默龍龜㵪䊚償儡優勵匵嚀嚄嚅嚇嚎嚐嚓壍壑壓壕嬰孺尷屨嶷嶸嶺嶽幫彌徽懋懦懨戲擊擎擘擠擡擢擣擦擩擫擬擯擰擱斁斂曒曖檀檄檎檐檔檗檠檢檣歛歜氈氉澀濕濛濟濠濡濤濩濫濮濯濱營燠燥燦燧燭燮牆獮獰獲璧璨璫環甑療癃癆癉盪瞤瞥瞧瞪瞬瞭瞰瞳瞵瞶矯磶磷磺磽礁礅禧禪穗窾窿篲篳篷簀簇簋糜糞糟糠糢糨縫縮縯縱縲縴縵縶縷縹縻總績繁繃繆繇罄罅翳聯聰聱聲聳膺膻膽膾膿臀臂臃臆臉臊臨艱蓬蓺蓼蓽蓿蔀蔌蔓蔗蔚蔞蔟蔡蔥蔫蔭蔴蔻薄虧螫螭螯螳螺螻螽螿蟀蟄蟆褵褸褻襁襄覬覯觳謅謇謊謎謏謔謖謗謙謚講謝謟謠谿豀豁貔賺賻購賽趨蹇蹈蹉蹊蹋蹌蹐蹓輾輿轂轄轅遽避邀邁邂邃還邅醜醞鍊鍋鍍鍔鍛鍥鍪鍵鍾闃闆闇闈闊闋闌隮隱隸雖霜霞鞞鞠韓顆颶餅餚餞館馘駴駸駿騁騂騃鮫鮮鴰鴻麋黈黏黛黜黝點黻黿鼾齋齔龠儲叢嚙嚚壘屩彝懣懩戳戴擲擴擷擺擻擾擿攄斃斷曙曜朦檮檻櫂櫃歟歸濺瀆瀉瀋燹燻燼燾爵獵璵璹甓甔甕癏癖皦盬瞻瞽瞿礉礌礎禮穟穠穡穢竄竅簞簟簠簡簣簦簧簪簫簬糧繈繒織繕繚繞繡繢翹翻翼聵職臍臏舊蔽蕃蕆蕉蕊蕓蕕蕖蕘蕙蕞蕢蕤蕩蕫蕭藉藍蟠蟣蟥蟬蟲覆觴謦謨謫謬謳謷謹謾豐賾贅蹕蹙蹚蹝蹠蹣蹤蹦軀轆轇轉邇邈醨醪醫醬釐鎔鎖鎞鎮鎰闐闔闕闖隳雙雛雜雞霣鞫鞬鞭韘韙題額顏顒顓颸颺餮餳馥騄騎騏髀鬅鬆鬩魋魍魎魏鯀鯁鯉鵑鵜鵝鵠鵡黠鼪鼫鼬䙡劖勷勸嚥嚨嚬嚮壚壞壟壢寵廬懲懵懶懷攀攏曝曠櫓櫛櫜櫝櫟櫥歠瀚瀝瀟瀡瀣瀧爆爇爍爕牘犢獸獹獻璺璽瓊瓣疆疇癡矇矱礙礡禱穩穫簷簸簾簿繩繪繫繭繮繯繰繳繹罊羅羆羶羸羹翾臘艤蕾薈薌薏薑薙薛薡薤薦薪藩蟒蟹蟻蟾蠃蠅蠆蠉蠍襖襛襞襟襠覈覷譁證譎譏譐譖識譚譜贈贊蹬蹭蹯蹱蹲蹴蹶蹺蹻軃轍轎轓辭辴邊醮醯醰鎩鏃鏈鏊鏌鏑鏖鏗鏘鏞鏟鏡鏤鏦關隴離難霧靡鞴鞵韜韝韞韻願顙顛顜類颻餺餼餿饁騖騙騞騤鬋鬍鯖鯢鯤鯨鯫鯰鵩鵬鵰鵲鵷鶂鶉麑麒麓麕麗麴黼齖齗龐䭔嚲嚴嚶嚷壤孀孽寶巇巉巋懸懺攔攖攘攙斅曦朧櫪櫬櫱瀲瀹瀽瀾爐犧獼瓌瓏癢癥矍礪礫竇競籃籋籌籍繻繼繽繾纂耀薩薰薸薺藁藋藎藏藐蘊蘋蘤蠐蠓蠕蠖襤襦覺觸警譬譭議贍贏躁躄躅躇轕轖醲醴醵釋鐉鐘鐙闞闡露響飄饅饈饉馨騫騮騰騶騷髊鬐鬒鯽鰈鰍鰓鶚鶤鶩鹹麵黥黧黨鼮鼯齜齞齟齠齡亹儷儸儹劗劘嚼囀囁囂屬巍懼懽懾攛攜攝斕曩櫻欃欄殲灌爛癩矑矓礱礴竈糲纇纊續纍纏罍羼藕藜藝藤藥藨藪蘭蠛蠟蠡蠢襪襮覼覽觺譴護譸譽贐贓躊躋躍轟辯酆醺鐫鐮鐵鐸鐺闢闥霸霹顧飆饋饌饎饑饒驀驁驂驅魑魔鰜鰥鶯鶱鶴鶵鶺鶻鶼鷁鷂鷃鷇麝黯鼙齎齦齧齩㩳䯢儻儼囅囈囉囊夔孊巒巔彎懿攞攢攧權歡灑灘爝瓤疊癬禳穰竊籙籜籟籠糱羇聽聾臞臟艫藹藺藻藿蘆蘇襲覿譾讀贖贗躐躑躓躕轡轢酈鑄鑊鑑鑒霽霾韁顫饔饕饗饘驊驍驕鬚鬻鰲鷗鷙鷚麞鼴齪齬龔儽巖巘戀戁戄攣攪攫斖曬欒癰皭籤籥籧纓纕纖蘖蘗蘧蘩蘿蠱蠲變讋讌讎讐躚轤邏邐鑞鑠鑣靨顯饜驗驚驛髒髓體鬟鱉鱗鷦鷯鷸鷺麟鼇鼷齃齏齰囑壩攬灝灞癲矗罐羈艷蠶蠹衋衢襶讒讓讕讖躞醽釀鑪靂靄靆靈顰驟鬢鬭魘鱠鱣鷹鸇鹽齅齶齷䍦廳斸欖灣籩籬籮糶纚纛臠蘺虀蠻襼觀觿躡躥釁鑰鑲靉顱鬣鸎鼉圞彠矚讚趲躧釃鑷饞驢黶䶥纜讜躩釅鑼鑽鑾鑿顴驤驥鬮鱷鱸黷戇欞豔驩鸚爨讟驪鬱鸝鸞灩'

character = '一'

urlPrefix = 'https://humanum.arts.cuhk.edu.hk/Lexis/lexi-mf/idiom.php?word='

counter = 1
# Define dataframe
df = pd.DataFrame(columns=['idiom', 'book1', 'book2', 'book3', 'book4', 'book5', 'book6', 'versatility'])

for character in allCharacters:
    print(f'{counter}/{len(allCharacters)}')
    url = urlPrefix + character
    data = requests.get(url).text

    # create BeautifulSoup object
    soup = BeautifulSoup(data, 'html.parser')

    # create list with all tables
    tables = soup.find_all('table')

    # Look for the table with id 'idiomTable'
    table = soup.find('table', id='idiomTable')

    # Exclude last row
    for row in table.find_all('tr'):
        try:
            # Find all data for each column
            columns = row.find_all('td')
            if columns != []:
                idiom = columns[0].text.strip()
                book1 = book_check(columns[1])
                book2 = book_check(columns[2])
                book3 = book_check(columns[3])
                book4 = book_check(columns[4])
                book5 = book_check(columns[5])
                book6 = book_check(columns[6])
                versatility = columns[7].text

                df = df._append({'idiom': idiom, 'book1': book1, 'book2': book2, 'book3': book3, 'book4': book4, 'book5': book5, 'book6': book6, 'versatility': versatility}, ignore_index=True)
        except:
            IndexError

    counter += 1

with open('chineseIdioms.csv', 'w', encoding='utf-8') as file:
    df.to_csv(file)

    

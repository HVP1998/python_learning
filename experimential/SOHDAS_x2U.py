# 将MATLAB中公式中的关于x的矩阵计算转变为关于U的矩阵计算
def x2U(equ:str)->str:
    res=list()
    for i in range(0,len(equ)):
        if(equ[i]=='U'):
            res.append(equ[i])
            res.append('.')
        elif(equ[i]=="."):
            pass
        else:
            res.append(equ[i])
    return "".join(res)


    

# equ="- (U^30*beta^29*k^35*x^2*954376433i)/2417851639229258349412352 + (588546761*U^28*beta^27*k^36*x^5)/94447329657392904273920 + (U^28*beta^27*k^35*x^5*778725611i)/70835497243044678205440 + (U^28*beta^27*k^35*x^4*999880613i)/226673591177742970257408 - (463017749*U^28*beta^27*k^34*x^4)/56668397794435742564352 + (16102946725*U^28*beta^27*k^34*x^3)/226673591177742970257408 + (U^28*beta^27*k^33*x^3*289856775i)/18889465931478580854784 + (U^28*beta^27*k^33*x^2*11877877851i)/302231454903657293676544 + (1002968853*U^28*beta^27*k^32*x^2)/75557863725914323419136 - (U^26*beta^25*k^37*x^9*1517326333193i)/104593038897933157662720 - (U^26*beta^25*k^37*x^8*11728839580823i)/743772721051969121157120 + (297016876824659*U^26*beta^25*k^36*x^10)/103393020549863120987750400 - (4555633731714179*U^26*beta^25*k^36*x^9)/1807367712156284964411801600 + (498640579319*U^26*beta^25*k^36*x^8)/46485795065748070072320 - (3664182725783*U^26*beta^25*k^36*x^7)/371886360525984560578560 - (U^26*beta^25*k^35*x^9*6887237105443i)/1035471085089538260860928 - (U^26*beta^25*k^35*x^8*182131611603029i)/32130981549445066033987584 - (U^26*beta^25*k^35*x^7*20480792977i)/3320413933267719290880 - (U^26*beta^25*k^35*x^6*9779712537449i)/212506491729134034616320 - (151960116033023*U^26*beta^25*k^34*x^8)/21388778392537340584132608 + (770555541909203*U^26*beta^25*k^34*x^7)/401637269368063325424844800 + (11869373697*U^26*beta^25*k^34*x^6)/1475739525896764129280 + (5287580126359*U^26*beta^25*k^34*x^5)/141670994486089356410880 + (U^26*beta^25*k^33*x^7*838435391620283i)/51466748007042975780569088 - (U^26*beta^25*k^33*x^6*126024521229937i)/76502337022488252461875200 + (U^26*beta^25*k^33*x^5*1950904573i)/2951479051793528258560 + (U^26*beta^25*k^33*x^4*584230548329i)/113336795588871485128704 + (4171431295120343*U^26*beta^25*k^32*x^6)/132343066303824794864320512 - (13076311683959*U^26*beta^25*k^32*x^5)/30600934808995300984750080 - (8386667983*U^24*beta^23*k^38*x^12)/933866418731546050560 - (3093990331*U^24*beta^23*k^38*x^11)/499359126682840596480 - (U^24*beta^23*k^37*x^13*2441235227849075i)/124096365879588140353585152 - (U^24*beta^23*k^37*x^12*3360221218357i)/31377911669379947298816000 + (U^24*beta^23*k^37*x^11*10929248321i)/7989746026925449543680 - (U^24*beta^23*k^37*x^10*28094203i)/2882303761517117440 + (4626286907428499*U^24*beta^23*k^36*x^13)/6057505847773798826036428800 + (4212269176556225*U^24*beta^23*k^36*x^12)/229100983162316556234391552 - (3766235672573473*U^24*beta^23*k^36*x^11)/94133735008139841896448000 - (4219660673329*U^24*beta^23*k^36*x^10)/43580432874138815692800 - (8419258639*U^24*beta^23*k^36*x^9)/217902164370694078464 + (U^24*beta^23*k^35*x^12*279217931226877i)/59169776290830757763481600 - (U^24*beta^23*k^35*x^11*2238900552684171i)/16291625469320290027700224 - (U^24*beta^23*k^35*x^10*98738953349797i)/1307412986224164470784000 - (U^24*beta^23*k^35*x^9*769470492355i)/3486434629931105255424 - (U^24*beta^23*k^35*x^8*845070445i)/4611686018427387904 + (5790864429807977*U^24*beta^23*k^34*x^11)/530161195565843589560795136 + (6057874655330369*U^24*beta^23*k^34*x^10)/63473865464884238382792704 - (40210661610913*U^24*beta^23*k^34*x^9)/261482597244832894156800 - (1664090062189*U^24*beta^23*k^34*x^8)/23242897532874035036160 + (8070046991*U^24*beta^23*k^34*x^7)/48422703193487572992 - (U^24*beta^23*k^33*x^10*8110697111936359i)/8262252398428731265882521600 - (U^24*beta^23*k^33*x^9*109608439704883i)/246650114739076595712000 - (U^24*beta^23*k^33*x^8*770838925216051i)/1793023523964568417075200 + (687579328730147*U^24*beta^23*k^32*x^9)/38729308117634677808824320 - (U^22*beta^21*k^39*x^15*5i)/5066549580791808 - (7688923158075591*U^22*beta^21*k^38*x^16)/2432882736751829885843931136 - (102193031*U^22*beta^21*k^38*x^15)/1489565576752791552000 + (5305*U^22*beta^21*k^38*x^14)/110338190870577152 + (25*U^22*beta^21*k^38*x^13)/4116571534393344 - (U^22*beta^21*k^37*x^16*827712258634633i)/80896178522620176629760000000 - (U^22*beta^21*k^37*x^15*8118428689598527i)/7602758552349467980945424384 - (U^22*beta^21*k^37*x^14*1397414693i)/7149914768413399449600 + (U^22*beta^21*k^37*x^13*9768625i)/11065344284449308672 + (U^22*beta^21*k^37*x^12*295i)/1266637395197952 - (5038786372253651*U^22*beta^21*k^36*x^15)/4147509152771053977600000000 - (5750731385895051*U^22*beta^21*k^36*x^14)/142551722856552528078700544 + (12953300203*U^22*beta^21*k^36*x^13)/12747276615685603590144 - (24719087*U^22*beta^21*k^36*x^12)/3404721318292094976 - (471*U^22*beta^21*k^36*x^11)/140737488355328 - (U^22*beta^21*k^35*x^14*38522365738231i)/900067090445107200000000 - (U^22*beta^21*k^35*x^13*5133854560906677i)/33092364234556836568629248 + (U^22*beta^21*k^35*x^12*1978511490541i)/49027986983406167654400 - (U^22*beta^21*k^35*x^11*81236809i)/4161326055690338304 + (388383733470227*U^22*beta^21*k^34*x^13)/41029032304705536000000000 - (6230493809858361*U^22*beta^21*k^34*x^12)/12218719101990216447033344 + (U^20*beta^19*k^39*x^19*2082300326347i)/252975076298667099150090240 - (84591157*U^20*beta^19*k^38*x^19)/3573817410551021568000 + (187234855920869*U^20*beta^19*k^38*x^18)/3235418081082952899656417280 - (U^20*beta^19*k^37*x^18*1034789807i)/3160006973539850649600 + (U^20*beta^19*k^37*x^17*6158951853746103i)/20052851648378719592173797376 + (26191232941*U^20*beta^19*k^36*x^17)/238756082445233160192000 + (6802776112078733*U^20*beta^19*k^36*x^16)/496665056306593646877081600 - (1411*U^20*beta^19*k^36*x^15)/18999560927969280 - (U^20*beta^19*k^35*x^16*2201394385781i)/16853370525545870131200000 - (U^20*beta^19*k^35*x^15*8357194203076839i)/3159587969807571465948626944"
# equ="- (493235465*U^26*beta^25*k^32*x^4)/7083549724304467820544 + (81796337955*U^26*beta^25*k^32*x^3)/37778931862957161709568 - (U^26*beta^25*k^31*x^5*7430981433351419i)/160415837944030054380994560 + (U^26*beta^25*k^31*x^4*52578949253233i)/40801246411993734646333440 + (U^26*beta^25*k^31*x^3*16654904585i)/7083549724304467820544 + (U^26*beta^25*k^31*x^2*109243026583i)/151115727451828646838272 - (5097528759685055*U^26*beta^25*k^30*x^4)/88228710869216529909547008 + (4572190889855*U^26*beta^25*k^30*x^3)/2720083094132915643088896 + (742731017*U^26*beta^25*k^30*x^2)/9444732965739290427392 + (U^26*beta^25*k^29*x^3*5099365523318245i)/88228710869216529909547008 - (U^24*beta^23*k^33*x^7*1063163794619i)/1291272085159668613120 - (U^24*beta^23*k^33*x^6*11121685775i)/27670116110564327424 + (77565478625737*U^24*beta^23*k^32*x^8)/365693052061061480448000 - (2519712585994811*U^24*beta^23*k^32*x^7)/33469772447338610452070400 + (5306288866669*U^24*beta^23*k^32*x^6)/6640827866535438581760 + (18463304433*U^24*beta^23*k^32*x^5)/18446744073709551616 + (U^24*beta^23*k^31*x^8*3801962288730667i)/783383931110279705209602048 - (U^24*beta^23*k^31*x^7*1070821221458531i)/3291237468549553324032000 - (U^24*beta^23*k^31*x^6*2416352131766333i)/3586047047929136834150400 - (U^24*beta^23*k^31*x^5*221454447689i)/885443715538058477568 + (6262384921967389*U^24*beta^23*k^30*x^7)/80327453873612665084968960 + (2719788991102669*U^24*beta^23*k^30*x^6)/5642121374656377126912000 - (U^22*beta^21*k^35*x^10*36001i)/1688849860263936 - (886664975462737*U^22*beta^21*k^34*x^11)/2696539284087339220992000 - (26946273577*U^22*beta^21*k^34*x^10)/340472131829209497600 + (437065*U^22*beta^21*k^34*x^9)/10133099161583616 - (U^22*beta^21*k^33*x^12*1602517188841441i)/2958824445050880000000000 - (U^22*beta^21*k^33*x^11*8029331991926929i)/2828407199534772186513408 - (U^22*beta^21*k^33*x^10*23430701565461i)/36317027395115679744000 - (U^22*beta^21*k^33*x^9*46301788097i)/81713311639010279424 - (U^22*beta^21*k^33*x^8*664265i)/4503599627370496 - (1223394982417*U^22*beta^21*k^32*x^11)/7086696038400000000000 - (1334766424589223*U^22*beta^21*k^32*x^10)/578537836268476153462784 - (290238074348555*U^22*beta^21*k^32*x^9)/141200602512209762844672 + (104717697083*U^22*beta^21*k^32*x^8)/181585136975578398720 - (U^22*beta^21*k^31*x^10*266567358367283i)/69347447930880000000000 - (U^22*beta^21*k^31*x^9*358389263499139i)/23802699549331591004160 - (U^20*beta^19*k^35*x^14*11639167i)/3723913941881978880 - (U^20*beta^19*k^35*x^13*625i)/4116571534393344 - (4945435577201923*U^20*beta^19*k^34*x^15)/41475091527710539776000000 + (150781303795013*U^20*beta^19*k^34*x^14)/359979098122607394816000 + (308070583*U^20*beta^19*k^34*x^13)/5927863009526415360 + (51845*U^20*beta^19*k^34*x^12)/8866461766385664 - (U^20*beta^19*k^33*x^14*2707627943340161i)/9216687006157897728000000 - (U^20*beta^19*k^33*x^13*1025157950019713i)/10696521772786047229362176 + (U^20*beta^19*k^33*x^12*9155315887i)/21279508239325593600 + (U^20*beta^19*k^33*x^11*909555i)/10836786603360256 - (81037493093147*U^20*beta^19*k^32*x^13)/26864247342366720000000 + (112956854629963*U^20*beta^19*k^32*x^12)/259834536990754209792000 - (U^18*beta^17*k^35*x^17*79620767034121i)/148539641839842359204904960 + (250220639*U^18*beta^17*k^34*x^17)/310880315683897344000 - (63665876119697*U^18*beta^17*k^34*x^16)/41940604754779019069620224 + (U^18*beta^17*k^33*x^16*641811223i)/48765539715121152000 - (U^18*beta^17*k^33*x^15*791437110374599i)/62411614218421159329792000"
# equ="- (U^26*beta^25*k^29*x^2*14777125838203i)/18133887294219437620592640 + (6799387192676911*U^26*beta^25*k^28*x^2)/156851041545273830950305792 + (U^24*beta^23*k^31*x^4*54826789195i)/73786976294838206464 + (937826656449983*U^24*beta^23*k^30*x^5)/2550077900749608415395840 + (2072576195219*U^24*beta^23*k^30*x^4)/3541774862152233910272 - (11605169845*U^24*beta^23*k^30*x^3)/73786976294838206464 - (U^24*beta^23*k^29*x^6*579145098581047i)/5100155801499216830791680 - (U^24*beta^23*k^29*x^5*4486840542889679i)/10030437999389114892288000 - (U^24*beta^23*k^29*x^4*4614090455895601i)/30600934808995300984750080 + (U^24*beta^23*k^29*x^3*465505387885i)/3541774862152233910272 + (U^24*beta^23*k^29*x^2*3735962655i)/295147905179352825856 - (4436031926895689*U^24*beta^23*k^28*x^5)/45901402213492951477125120 - (6885475883964713*U^24*beta^23*k^28*x^4)/24073051198533875741491200 + (2287087625525711*U^24*beta^23*k^28*x^3)/30600934808995300984750080 + (58607273325*U^24*beta^23*k^28*x^2)/4722366482869645213696 + (U^24*beta^23*k^27*x^4*1430904542742661i)/10880332376531662572355584 + (U^24*beta^23*k^27*x^3*2965925510225221i)/7703376383530840237277184 + (U^24*beta^23*k^27*x^2*224024790523441i)/40801246411993734646333440 + (5719623671251273*U^24*beta^23*k^26*x^3)/36721121770794361181700096 + (3221304841553023*U^24*beta^23*k^26*x^2)/11204911103317585799675904 - (U^24*beta^23*k^25*x^2*457769225545567i)/4080124641199373464633344 + (12522305*U^22*beta^21*k^32*x^7)/15762598695796736 - (U^22*beta^21*k^31*x^8*23140601269567i)/2905362191609254379520 - (U^22*beta^21*k^31*x^7*232083108923i)/90792568487789199360 + (U^22*beta^21*k^31*x^6*5983935i)/9007199254740992 - (2020492638284023*U^22*beta^21*k^30*x^9)/7608405715845120000000000 + (1017375030347539*U^22*beta^21*k^30*x^8)/211579551549614142259200 + (13699298050897*U^22*beta^21*k^30*x^7)/10459303889793315766272 + (305466018757*U^22*beta^21*k^30*x^6)/51881467707308113920 + (38933565*U^22*beta^21*k^30*x^5)/18014398509481984 - (U^22*beta^21*k^29*x^8*1170086766277771i)/110955916689408000000000 - (U^22*beta^21*k^29*x^7*456650304419941i)/15300174182306807808000 - (U^22*beta^21*k^29*x^6*32934221522713i)/1844674407370955161600 + (U^22*beta^21*k^29*x^5*5852124991i)/6917529027641081856 + (U^22*beta^21*k^29*x^4*359597775i)/72057594037927936 + (527730544205717*U^22*beta^21*k^28*x^7)/208042343792640000000000 + (5339037613687139*U^22*beta^21*k^28*x^6)/528948878874035355648000 + (72760603137391*U^22*beta^21*k^28*x^5)/3984496719921263149056 + (63652139369*U^22*beta^21*k^28*x^4)/9223372036854775808 - (274386225*U^22*beta^21*k^28*x^3)/72057594037927936 - (U^22*beta^21*k^27*x^6*268752983783279i)/19021014289612800000000 - (U^22*beta^21*k^27*x^5*1315648227243847i)/141053034366409428172800 + (U^22*beta^21*k^27*x^4*13134938301737i)/79689934398425262981120 + (U^22*beta^21*k^27*x^3*164177808325i)/27670116110564327424 + (3749263857697897*U^22*beta^21*k^26*x^5)/1268067619307520000000000 + (5546526865250051*U^22*beta^21*k^26*x^4)/282106068732818856345600 - (6063107159731*U^20*beta^19*k^32*x^11)/3511118859488722944000 - (40465741*U^20*beta^19*k^32*x^10)/75998243711877120 - (U^20*beta^19*k^31*x^12*3024787748742709i)/315607940805427200000000 - (U^20*beta^19*k^31*x^11*7626451589639015i)/530326349912769818525696 - (U^20*beta^19*k^31*x^10*1659521539133i)/1276770494359535616000 - (U^20*beta^19*k^31*x^9*227956405i)/212795082393255936 - (742363616726411*U^20*beta^19*k^30*x^11)/30136174903296000000000 - (7684627370464867*U^20*beta^19*k^30*x^10)/385691890845650813714432 - (10334354233027*U^20*beta^19*k^30*x^9)/656624825670618316800 - (343540213*U^20*beta^19*k^30*x^8)/94575592174780416 - (U^20*beta^19*k^29*x^10*140665517239999i)/1467670855680000000000 - (U^20*beta^19*k^29*x^9*4185741348809i)/27993766271055298560 - (U^20*beta^19*k^29*x^8*105912508419911i)/2042832790975256985600 - (U^20*beta^19*k^29*x^7*2755121825i)/141863388262170624 - (192802002618629*U^20*beta^19*k^28*x^9)/2568423997440000000000 + (6280937281144901*U^20*beta^19*k^28*x^8)/1234214050706082496512000 + (2079847148579*U^20*beta^19*k^28*x^7)/340472131829209497600 + (430256501*U^20*beta^19*k^28*x^6)/27021597764222976 - (U^20*beta^19*k^27*x^8*509047246802491i)/1320903770112000000000 + (141394804931*U^18*beta^17*k^32*x^15)/2618376990385766400000 - (6092184934972967*U^18*beta^17*k^32*x^14)/11795795087281599113330688 + (79*U^18*beta^17*k^32*x^13)/24120536334336 + (U^18*beta^17*k^31*x^14*36528594902441i)/46083435030789488640000 - (U^18*beta^17*k^31*x^13*4015868011123i)/7886836330164828241920 + (U^18*beta^17*k^31*x^12*82717i)/692692325498880 + (U^18*beta^17*k^31*x^11*25i)/4535485464576 - (5872449031765553*U^18*beta^17*k^30*x^13)/3423340888001504870400000 - (90660032044031*U^18*beta^17*k^30*x^12)/5774100822016760217600 - (180445081*U^18*beta^17*k^30*x^11)/114294233707315200 - (781*U^18*beta^17*k^30*x^10)/4947802324992 - (U^18*beta^17*k^29*x^12*1902971017639709i)/379200836824782077952000 - (U^18*beta^17*k^29*x^11*4105208315027851i)/84686812056245816524800 - (U^18*beta^17*k^29*x^10*357861929i)/41561539529932800 - (1639719065801461*U^18*beta^17*k^28*x^11)/14465363953582080000000 + (U^16*beta^15*k^31*x^15*428698786919i)/56623440319132100198400 - (174569389*U^16*beta^15*k^30*x^15)/3000223634817024000 + (740971824217837*U^16*beta^15*k^30*x^14)/9829829239401332594442240 + (U^16*beta^15*k^29*x^14*2259769i)/17779103021137920"
equ="(+ (157730514973141*U^22*beta^21*k^26*x.^3)/15937986879685052596224 - (57919353915*U^22*beta^21*k^26*x.^2)/36893488147419103232 + (596604821678263*U^22*beta^21*k^24*x.^3)/135260546059468800000000 - (7560796092728357*U^22*beta^21*k^24*x.^2)/1504565699908367233843200 + (2663019620875601*U^20*beta^19*k^26*x.^7)/277389791723520000000000 + (313544437700509*U^20*beta^19*k^26*x.^6)/1224418701097304064000 + (3582624611983*U^20*beta^19*k^26*x.^5)/15564440312192434176 + (8162896055*U^20*beta^19*k^26*x.^4)/72057594037927936 + (799692171324739*U^20*beta^19*k^24*x.^5)/5283615080448000000000 + (1195253925695993*U^20*beta^19*k^24*x.^4)/4701767812213647605760 + (27737030450569*U^20*beta^19*k^24*x.^3)/311288806243848683520 - (2844236325*U^20*beta^19*k^24*x.^2)/288230376151711744 + (753057841243393*U^20*beta^19*k^22*x.^3)/8453784128716800000000 + (5320446505500083*U^20*beta^19*k^22*x.^2)/94035356244272952115200 - (265240458005107*U^18*beta^17*k^28*x.^10)/2448837402194608128000 + (1380635737*U^18*beta^17*k^28*x.^9)/149621542307758080 + (59035*U^18*beta^17*k^28*x.^8)/13194139533312 - (1317927475896793*U^18*beta^17*k^26*x.^9)/1183529778020352000000 - (573037305905447*U^18*beta^17*k^26*x.^8)/7836279687022746009600 + (664582055*U^18*beta^17*k^26*x.^7)/3324923162394624 + (2120995*U^18*beta^17*k^26*x.^6)/26388279066624 - (3413210811619439*U^18*beta^17*k^24*x.^7)/4566087106560000000000 + (742607965466419*U^18*beta^17*k^24*x.^6)/391813984351137300480 + (600380967*U^18*beta^17*k^24*x.^5)/703687441776640 + (19801425*U^18*beta^17*k^24*x.^4)/70368744177664 + (2335101838696661*U^18*beta^17*k^22*x.^5)/2201506283520000000000 + (2532852367340153*U^18*beta^17*k^22*x.^4)/1044837291603032801280 + (1377564083*U^18*beta^17*k^22*x.^3)/1688849860263936 - (455610874933*U^16*beta^15*k^28*x.^13)/29716500763901952000 + (7641764767335191*U^16*beta^15*k^28*x.^12)/1053195989935857063690240 + (215*U^16*beta^15*k^28*x.^11)/6803228196864 - (63064535118463*U^16*beta^15*k^26*x.^11)/146949729052262400000 + (1392858945981913*U^16*beta^15*k^26*x.^10)/26120932290075820032000 - (913067*U^16*beta^15*k^26*x.^9)/311711546474496 - (2559919901690761*U^16*beta^15*k^24*x.^9)/526013234675712000000 - (74773174707269*U^16*beta^15*k^24*x.^8)/1924700274005586739200 - (106203169*U^16*beta^15*k^24*x.^7)/346346162749440 - (5289220181243617*U^16*beta^15*k^22*x.^7)/308210879692800000000 + (116072311*U^14*beta^13*k^26*x.^13)/7738672073932800 + (3880006336649*U^14*beta^13*k^26*x.^12)/4388316624732737765376 + (375294191*U^14*beta^13*k^24*x.^11)/1195879956480000 + (5355690991735267*U^14*beta^13*k^24*x.^10)/58510888329769836871680 - (5*U^14*beta^13*k^24*x.^9)/14495514624)"
res=x2U(equ)
print(res)

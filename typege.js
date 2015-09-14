//All possible gearea  ["A" - "g", "EUR", "WRT", "WOR", 'ETH', "DEP", 'QUR']


/*geReq = [
    {
        type : "ENGR",

        geAreas : [{type : "areas", areas : ["D","E"], number :"2"},
                   {type : "areas", areas : ["F","G"], number : "2"},
                   {type : "areas", areas : ["D","E","F","G","H"], number:"6"}
        ],

        otherReq : [{type : "ethnicity", number : "1"},
                    {type : "writing",   number : "4"},
                    {type : "europeanTraditions", number : "1"},
                    {type : "depth", choices : [{type : "upper", number : "2"},
                                                {type : "sequence", number : "3"},
                                                {type : "minor", number : "1"}
                                                ]}]
    },

    {
        type :"LSBA",

        geAreas : [{type : "area", area : "C", number : "3"},
                   {type : "area", area : "D", number : "3"},
                   {type : "area", area : "E", number : "3"},
                   {type : "area", area : "F", number : "2"},
                   {type : "area", area : "G", number : "2"}
        ],

        otherReq : [{type : "worldCulturesRequirment", number : "1"},
                    {type : "writing",   number : "6"},
                    {type : "europeanTraditions", number : "1"},
                    {type : "quantitativeRelationships", number : "1"},
                    {type : "ethnicity", number : "1"}
                    ]
    },

    {
        type : "LSBS",

        geAreas : [{type : "area", area : "C", number : "3"},
                   {type : "area", area : "D", number : "2"},
                   {type : "area", area : "E", number : "2"},
                   {type : "area", area : "F", number : "1"},
                   {type : "area", area : "G", number : "1"}
        ],

        otherReq : [{type : "worldCulturesRequirment", number : "1"},
                    {type : "writing",   number : "6"},
                    {type : "quantitativeRelationships", number : "1"},
                    {type : "ethnicity", number : "1"}
                    ]
    },


    {
        type : "BMFA",

        geAreas : [{type : "area", area : "C", number : "2"},
                   {type : "area", area : "D", number : "2"},
                   {type : "area", area : "E", number : "2"},
                   {type : "area", area : "G", number : "1"}
        ],

        otherReq : [{type : "worldCulturesRequirment", number : "1"},
                    {type : "writing",   number : "6"},
                    {type : "quantitativeRelationships", number : "1"},
                    {type : "ethnicity", number : "1"}
                    ]
    }

]

var user = {
    major : "Computer Science",
    majorType : "ENGR"
}



var geStatus  = {
    gearea : [{area : "A", taken :0},
              {area : "B", taken :0},
              {area : "C", taken :0},
              {area : "D", taken :0},
              {area : "E", taken :0},
              {area : "F", taken :0},
              {area : "G", taken :0}
    ],
    otherReq : [ {type : "worldCulturesRequirment", taken : 0},
                 {type : "writing",   taken : 0},
                 {type : "europeanTraditions", taken : 0},
                 {type : "quantitativeRelationships", taken : 0},
                 {type : "ethnicity", taken : 0},
                 {type : "depth", taken :0}
    ]
}
*/
//global variable you should provide
var user = {
    major : "Computer Science",
    majorType : "ENGR"
}


//local variable to count the ge requirment



var geStatus =new Array() 
    geStatus["A"] = 0,
    geStatus["B"] = 0,
    geStatus["C"] = 0,
    geStatus["D"] = 0,
    geStatus["E"] = 0,
    geStatus["F"] = 0,
    geStatus["G"] = 0,
    geStatus["H"] = 0,

    geStatus["EUR"] = 0,
    geStatus["WRT"] = 0,
    geStatus["WOR"] = 0,
    geStatus["ETH"] = 0,
    geStatus["DEP"] = 0,
    geStatus["QUR"] = 0


var depth = false


var reqNumber = [
            [2,2,6,1,4,1,1],
            [3,3,3,2,2,1,6,1,1,1],
            [3,2,2,1,1,1,6,1,1],
            [2,2,2,1,1,6,1,1]
 ]

var depthSequence = [
    {sub : "CH ST", number : ["1A",  "1B",  "1C" ]},
    {sub : "C LIT", number : ["30A", "30B", "30C"]},
    {sub : "FR",    number : ["50AX", "50BX", "50CX"]},
    {sub : "HIST",  number : ["2A",  "2B",  "2C" ]},
    {sub : "HIST",  number : ["2AH", "2BH", "2CH"]},
    {sub : "HIST",  number : ["4A",  "4B",  "4C" ]},
    {sub : "HIST",  number : ["4AH", "4BH", "4CH"]},
    {sub : "HIST",  number : ["17A", "17B", "17C"]},
    {sub : "HIST",  number : ["17AH","17BH","17CH"]},
    {sub : "PHIL",  number : ["20A" , "20B", "20C"]},
    {sub : "RG ST", number : ["80A",  "80B", "80C"]},
    {sub : "ARTHI", number : ["6A", "6B", "6C", "6D", "6DS", "6DW", "6E", "6F", "6G", "6H", "6K"]}
]



function UpdateGE(){
    for(area of geStatus)
        area = 0

    for(course of validCourses){
        for(ge of course.gearea)
            geStatus[ge]+=1
    }
    console.log("ge",geStatus)

    if(user.majorType=="ENGR"){
        checkDepth()
    }
}

function checkDepth(){
    var count = 0
    for(seq of depthSequence){
        for(course of validCourses){
            if(course.sub == seq.sub){
                for(number of seq.number){
                    if(course.number == number){
                        count+=1
                        break
                    }
                }
            }
        }
        if(count>=3){
            depth=true
            break
        }
        count = 0
        if(depth)
            break
    }
    if(depth)
        return

    count = 0
    var firstUpper = ""
    for(course of validCourses){
        if(parseInt(course.number)>99){
            if(course.gearea.indexOf("D")>-1 || course.gearea.indexOf("E")>-1 ||course.gearea.indexOf("F")>-1 
                ||course.gearea.indexOf("G")>-1 ||course.gearea.indexOf("H")>-1){
                if(count==0||course.sub!=firstUpper){
                    count++
                    firstUpper = course.sub
                }
            }
        }
        if(count>=2){
            depth = true
            break
        }
    }

}



function ValidGE(){
    UpdateGE()
    var w2 = false, w50 = false
    for(course of validCourses){
        if(course.sub == "WRIT"&&course.number.slice(0,1)=="2"){
            w2 = true
            break
        }
    }
    for(course of validCourses){
        if(course.sub == "WRIT"&&(course.number.slice(0,2)=="50"||course.number.slice(0,4)=="109")){
            w50 = true
            break
        }
        if(course.sub == "ENGL"&&course.number.slice(0,3)=="10"){
            w50 = true
            break
        }
    }



    if(user.majorType=="ENGR"){
        var geFullFillment = [
                          {type : "Area D,E", status : (geStatus["D"]+geStatus["E"])>=reqNumber[0][0], 
                                 message : (geStatus["D"]+geStatus["E"]) +"/2"},
                          {type : "Area F,G", status : (geStatus["F"]+geStatus["G"])>=reqNumber[0][1], 
                                 message : (geStatus["F"]+geStatus["G"])+"/2"},
                          {type : "Area D,E,F,G,H", status : (geStatus["D"]+geStatus["E"]+geStatus["F"]+geStatus["G"]+geStatus["H"])>=reqNumber[0][2], 
                                 message : (geStatus["D"]+geStatus["E"]+geStatus["F"]+geStatus["G"]+geStatus["H"]) +"/6"},
                          {type : "ETH", status : (geStatus["ETH"])>=reqNumber[0][3], message :(geStatus["ETH"])+"/1"},
                          {type : "WRT", status :(geStatus["WRT"])>=reqNumber[0][4], message : (geStatus["WRT"])+"/4"},
                          {type : "EUR", status : (geStatus["EUR"])>=reqNumber[0][5], message : (geStatus["EUR"])+"/1"},
                          {type : "DEP", status : depth, message : (depth ? "1":"0") + "/1"},
                          {type : "WRIT 2", status : w2, message : (w2? "1": "0") + "/1"},
                          {type : "WRIT 50", status : w50, message : (w50? "1" : "0")+ "/1"},
        ]
        console.log("geFullFillment",geFullFillment)
        return geFullFillment
    }

    else if(user.majorType == "LSBA"){
        var geFullFillment = [{type : "WRIT 2", status : w2, message : (w2? "1": "0") + "/1"},
                          {type : "WRIT 50", status : w50, message : (w50? "1" : "0")+ "/1"},
                          {type : "Area C", status :(geStatus["C"]>=reqNumber[1][0]), message :geStatus.gearea[2].taken+"/3"},
                          {type : "Area D", status :(geStatus["D"]>=reqNumber[1][1]), message :geStatus.gearea[3].taken+"/3"},
                          {type : "Area E", status :(geStatus["E"]>=reqNumber[1][2]), message :geStatus.gearea[4].taken+"/3"},
                          {type : "Area F", status :(geStatus["F"]>=reqNumber[1][3]), message :geStatus.gearea[5].taken+"/2"},
                          {type : "Area G", status :(geStatus["G"]>=reqNumber[1][4]), message :geStatus.gearea[6].taken+"/2"},
                          {type : "WOR", status : (geStatus["WOR"]>=reqNumber[1][5]), message : (geStatus.otherReq[0].taken)+"/1"},
                          {type : "WRT", status : (geStatus["WRT"])>=reqNumber[1][6], message : (geStatus.otherReq[1].taken)+"/6"},
                          {type : "EUR", status : (geStatus["EUR"]>=reqNumber[1][7]), message : (geStatus.otherReq[2].taken)+"/1"},
                          {type : "QUR", status : (geStatus.otherReq[3].taken>=reqNumber[1][8]), message : (geStatus.otherReq[3].taken)+"/1"},
                          {type : "ETH", status : (geStatus.otherReq[4].taken>=reqNumber[1][9]), message : (geStatus.otherReq[4].taken)+"/1"}
        ]
        return geFullFillment

    }

    else if(user.majorType == "LSBS"){
        var geFullFillment = [{type : "WRIT 2", status : w2, message : (w2? "1": "0") + "/1"},
                          {type : "WRIT 50", status : w50, message : (w50? "1" : "0")+ "/1"},
                          {type : "AreaC", status :(geStatus.gearea[2].taken>=reqNumber[2][0]), message :geStatus.gearea[2].taken+"/3"},
                          {type : "Area D", status :(geStatus.gearea[3].taken>=reqNumber[2][1]), message :geStatus.gearea[3].taken+"/2"},
                          {type : "Area E", status :(geStatus.gearea[4].taken>=reqNumber[2][2]), message :geStatus.gearea[4].taken+"/2"},
                          {type : "Area F", status :(geStatus.gearea[5].taken>=reqNumber[2][3]), message :geStatus.gearea[5].taken+"/1"},
                          {type : "Area G", status :(geStatus.gearea[6].taken>=reqNumber[2][4]), message :geStatus.gearea[6].taken+"/1"},
                          {type : "WOR", status : (geStatus.otherReq[0].taken>=reqNumber[2][5]), message :(geStatus.otherReq[0].taken)+"/1"},
                          {type : "WRT", status : (geStatus.otherReq[1].taken)>=reqNumber[2][6], message :(geStatus.otherReq[1].taken)+"/6"},
                          {type : "QUR", status : (geStatus.otherReq[3].taken>=reqNumber[2][7]), message :(geStatus.otherReq[3].taken)+"/1"},
                          {type : "ETH", status : (geStatus.otherReq[4].taken>=reqNumber[2][8]), message :(geStatus.otherReq[4].taken)+"/1"}
        ]
        console.log("geFullFillment",geFullFillment)
        return geFullFillment
    }

    else if(user.majorType == "BMFA"){
        var geFullFillment = [{type : "WRIT 2", status : w2, message : (w2? "1": "0") + "/1"},
                          {type : "WRIT 50", status : w50, message : (w50? "1" : "0")+ "/1"},
                          {type : "Area C", status :(geStatus.gearea[2].taken>=reqNumber[3][0]), message :geStatus.gearea[2].taken+"/2"},
                          {type : "Area D", status :(geStatus.gearea[3].taken>=reqNumber[3][1]), message :geStatus.gearea[3].taken+"/2"},
                          {type : "Area E", status :(geStatus.gearea[4].taken>=reqNumber[3][2]), message :geStatus.gearea[4].taken+"/2"},
                          {type : "Area G", status :(geStatus.gearea[6].taken>=reqNumber[3][3]), message :geStatus.gearea[6].taken+"/1"},
                          {type : "WOR", status : (geStatus.otherReq[0].taken>=reqNumber[3][4]), message :(geStatus.otherReq[0].taken)+"/1"},
                          {type : "WRT", status : (geStatus.otherReq[1].taken)>=reqNumber[3][5], message :(geStatus.otherReq[1].taken)+"/6"},
                          {type : "QUR", status : (geStatus.otherReq[3].taken>=reqNumber[3][6]), message :(geStatus.otherReq[3].taken)+"/1"},
                          {type : "ETH", status : (geStatus.otherReq[4].taken>=reqNumber[3][7]), message :(geStatus.otherReq[4].taken)+"/1"}
        ]
        return geFullFillment
    }
    console.log("geFullFillment",geFullFillment)


}









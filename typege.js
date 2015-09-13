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
	majorType : "LSBS"
}


//local variable to count the ge requirment
var geStatus  = {
	gearea : [{area : "A", taken :0},
	          {area : "B", taken :0},
	          {area : "C", taken :0},
	          {area : "D", taken :0},
	          {area : "E", taken :0},
	          {area : "F", taken :0},
	          {area : "G", taken :0},
	          {area : "H", taken :0}
	],
	otherReq : [ {type : "worldCulturesRequirment", taken : 0},
		         {type : "writing",   taken : 0},
		         {type : "europeanTraditions", taken : 0},
		         {type : "quantitativeRelationships", taken : 0},
		         {type : "ethnicity", taken : 0},
		         {type : "depth", taken :0}
	]
}

function UpdateGE(){
	for(area of geStatus.gearea)
		area.taken = 0

	for(req of geStatus.otherReq)
		req.taken = 0

	for(course of validCourses){
		for(ge of course.gearea)
			switch (ge){
				case "A":
					geStatus.gearea[0].taken+=1
					break
				case "B":
					geStatus.gearea[1].taken+=1
					break
				case "C":
					geStatus.gearea[2].taken+=1
					break
				case "D":
					geStatus.gearea[3].taken+=1
					break
				case "E":
					geStatus.gearea[4].taken+=1
					break
				case "F":
					geStatus.gearea[5].taken+=1
					break
				case "G":
					geStatus.gearea[6].taken+=1
					break
				case "h":
					geStatus.gearea[7].taken+=1
					break
				case "WOR":
					geStatus.otherReq[0].taken+=1
					break
				case "WRT":
					geStatus.otherReq[1].taken+=1
					break
				case "EUR":
					geStatus.otherReq[2].taken+=1
					break
				case "QUR":
					geStatus.otherReq[3].taken+=1
					break
				case "ETH":
					geStatus.otherReq[4].taken+=1
					break

			}
	}
	console.log("ge",geStatus)
}



function ValidGE(){
	UpdateGE()
	if(user.majorType=="ENGR"){
		var geFullFillment = [{type : "Area D,E", status : false, 
		                         message : (geStatus.gearea[3].taken+geStatus.gearea[4].taken) +"/2"},
		                  {type : "Area F,G", status : false, 
		                         message : (geStatus.gearea[5].taken+geStatus.gearea[6].taken)+"/2"},
		                  {type : "Area D,E,F,G,H", status : false, 
		                         message : (geStatus.gearea[3].taken+geStatus.gearea[4].taken+geStatus.gearea[5].taken+geStatus.gearea[6].taken+geStatus.gearea[7].taken) +"/6"},
		                  {type : "ETH", status : false, message :(geStatus.otherReq[4].taken)+"/1"},
		                  {type : "WRT", status :false, message : (geStatus.otherReq[1].taken)+"/4"},
		                  {type : "EUR", status : false, message : (geStatus.otherReq[2].taken)+"/1"},
		                  {type : "DEP", status :false, message : (geStatus.otherReq[5].taken)+"/1"}
		]
		if((geStatus.gearea[3].taken+geStatus.gearea[4].taken)>=2)
			geFullFillment[0].status = true
		if((geStatus.gearea[5].taken+geStatus.gearea[6].taken)>=2)
			geFullFillment[1].status = true
		if((geStatus.gearea[3].taken+geStatus.gearea[4].taken+geStatus.gearea[5].taken+geStatus.gearea[6].taken+geStatus.gearea[7].taken)>=6)
			geFullFillment[2].status = true
		if((geStatus.otherReq[4].taken)>=1)
			geFullFillment[3].status = true
		if((geStatus.otherReq[1].taken)>=4)
			geFullFillment[4].status = true
		if((geStatus.otherReq[2].taken)>=1)
			geFullFillment[5].status = true
		if((geStatus.otherReq[5].taken)>=1)
			geFullFillment[6].status = true
		console.log("geFullFillment",geFullFillment)
		return geFullFillment
	}

	else if(user.majorType == "LSBA"){
		var geFullFillment = [{type : "Area C", status :(geStatus.gearea[2].taken>=3), message :geStatus.gearea[2].taken+"/3"},
		                  {type : "Area D", status :(geStatus.gearea[3].taken>=3), message :geStatus.gearea[3].taken+"/3"},
		                  {type : "Area E", status :(geStatus.gearea[4].taken>=3), message :geStatus.gearea[4].taken+"/3"},
		                  {type : "Area F", status :(geStatus.gearea[5].taken>=2), message :geStatus.gearea[5].taken+"/2"},
		                  {type : "Area G", status :(geStatus.gearea[6].taken>=2), message :geStatus.gearea[6].taken+"/2"},
		                  {type : "WOR", status : (geStatus.otherReq[0].taken>=1), message : (geStatus.otherReq[0].taken)+"/1"},
		                  {type : "WRT", status : (geStatus.otherReq[1].taken)>=6, message : (geStatus.otherReq[1].taken)+"/6"},
		                  {type : "EUR", status : (geStatus.otherReq[2].taken>=1), message : (geStatus.otherReq[2].taken)+"/1"},
		                  {type : "QUR", status : (geStatus.otherReq[3].taken>=1), message : (geStatus.otherReq[3].taken)+"/1"},
		                  {type : "ETH", status : (geStatus.otherReq[4].taken>=1), message : (geStatus.otherReq[4].taken)+"/1"}
		]
		return geFullFillment

	}

	else if(user.majorType == "LSBS"){
		var geFullFillment = [{type : "AreaC", status :(geStatus.gearea[2].taken>=3), message :geStatus.gearea[2].taken+"/3"},
		                  {type : "Area D", status :(geStatus.gearea[3].taken>=2), message :geStatus.gearea[3].taken+"/2"},
		                  {type : "Area E", status :(geStatus.gearea[4].taken>=2), message :geStatus.gearea[4].taken+"/2"},
		                  {type : "Area F", status :(geStatus.gearea[5].taken>=1), message :geStatus.gearea[5].taken+"/1"},
		                  {type : "Area G", status :(geStatus.gearea[6].taken>=1), message :geStatus.gearea[6].taken+"/1"},
		                  {type : "WOR", status : (geStatus.otherReq[0].taken>=1), message :(geStatus.otherReq[0].taken)+"/1"},
		                  {type : "WRT", status : (geStatus.otherReq[1].taken)>=6, message :(geStatus.otherReq[1].taken)+"/6"},
		                  {type : "QUR", status : (geStatus.otherReq[3].taken>=1), message :(geStatus.otherReq[3].taken)+"/1"},
		                  {type : "ETH", status : (geStatus.otherReq[4].taken>=1), message :(geStatus.otherReq[4].taken)+"/1"}
		]
		console.log("geFullFillment",geFullFillment)
		return geFullFillment
	}

	else if(user.majorType == "BMFA"){
		var geFullFillment = [{type : "Area C", status :(geStatus.gearea[2].taken>=2), message :geStatus.gearea[2].taken+"/2"},
		                  {type : "Area D", status :(geStatus.gearea[3].taken>=2), message :geStatus.gearea[3].taken+"/2"},
		                  {type : "Area E", status :(geStatus.gearea[4].taken>=2), message :geStatus.gearea[4].taken+"/2"},
		                  {type : "Area G", status :(geStatus.gearea[6].taken>=1), message :geStatus.gearea[6].taken+"/1"},
		                  {type : "WOR", status : (geStatus.otherReq[0].taken>=1), message :(geStatus.otherReq[0].taken)+"/1"},
		                  {type : "WRT", status : (geStatus.otherReq[1].taken)>=6, message :(geStatus.otherReq[1].taken)+"/6"},
		                  {type : "QUR", status : (geStatus.otherReq[3].taken>=1), message :(geStatus.otherReq[3].taken)+"/1"},
		                  {type : "ETH", status : (geStatus.otherReq[4].taken>=1), message :(geStatus.otherReq[4].taken)+"/1"}
		]
		return geFullFillment
	}
	console.log("geFullFillment",geFullFillment)


}

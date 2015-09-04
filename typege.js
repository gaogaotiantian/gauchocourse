geReq = [
	{
		type : "ENGR",

		geAreas : [{type : "areas", areas : ["D","E"], number :"2"},
                   {type : "areas", areas : ["F","G"], number : "2"},
                   {type : "areas", areas : ["D","E","F","G","H"], number:"6"}
		],

		OtherReq : [{type : "ethnicity", number : "1"},
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

		OtherReq : [{type : "worldCulturesRequirment", number : "1"},
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

		OtherReq : [{type : "worldCulturesRequirment", number : "1"},
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

		OtherReq : [{type : "worldCulturesRequirment", number : "1"},
		            {type : "writing",   number : "6"},
		            {type : "quantitativeRelationships", number : "1"},
		            {type : "ethnicity", number : "1"}
		            ]
	}

]
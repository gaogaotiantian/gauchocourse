var course1 = {
    label : "CMPSC 8 Introduction to Computer Science",
    sub: "CMPSC",
    id : "8",
    prereq : [{sub : "Math", id : "3A", concur : "y"}],
    unit :4,
    semester : {"spring":"y", "summer":"y", "fall":"y", "winter":"y"}
}

var course2 = {
    label :"CMPSC 16 Problem Solving with Computers I",
    sub : "CMPSC",
    id : "16",
    units : "4",
    prereq : [{sub : "MATH",  id : "3A",  concur : "y"}, {sub : "CMPSC", id :"8", concur :"n"}],
    semester : {"spring":"y", "summer":"y", "fall":"y", "winter":"y"}

}

var course3 = {
    label :"Math 3A, Introduction to Calclus",
    sub : "Math",
    id : "3A",
    units : "4",
    prereq : [],
    semester : {"spring":"y", "summer":"y", "fall":"y", "winter":"y"}

}



var inputCourses = [
                    {name : "CMPSC8", semester : "freshmenFall"},
                    {name : "CMPSC16", semester : "freshmenWinter"},
                    {name : "Math3A", semester : "freshmenFall"}
]

    var allCourses  = [course1,course2,course3]
    var addedCourses = []
    var schedule = []
    var error = []

    function SemToNum(semester){
    if(semester == "freshmenSummer") return 0;
    if(semester == "freshmenFall") return 1;
    if(semester == "freshmenWinter") return 2;
    if(semester == "freshmenSpring") return 3;
    if(semester == "sophomoreSummer") return 4;
    if(semester == "sophomoreFall") return 5;
    if(semester == "sophomoreWinter") return 6;
    if(semester == "sophomoreSpring") return 7;
    if(semester == "juniorSummer") return 8;
    if(semester == "juniorFall") return 9;
    if(semester == "juniorWinter") return 10;
    if(semester == "juniorSpring") return 11;
    if(semester == "seniorSummer") return 12;
    if(semester == "seniorFall") return 13;
    if(semester == "seniorWinter") return 14;
    if(semester == "seniorSpring") return 15;
}

    function NumToSem(num){
        if(num==0) return  "freshmenSummer";
        if(num==1) return "freshmenFall";
        if(num==2) return "freshmenWinter";
        if(num==3) return "freshmenSpring";
        if(num==4) return "sophomoreSummer";
        if(num==5) return "sophomoreFall";
        if(num==6) return "sophomoreWinter";
        if(num==7) return "sophomoreSpring";
        if(num==8) return "juniorSummer";
        if(num==9) return "juniorFall";
        if(num==10) return "juniorWinter";
        if(num==11) return "juniorSpring";
        if(num==12) return "seniorSummer";
        if(num==13) return "seniorFall";
        if(num==14) return "seniorWinter";
        if(num==15) return "seniorSpring";
    }

function AddAllCourses(input, all){
    for(i=0; i<input.length;i++){
        for(j=0; j<all.length; j++){
            var temp = (all[j].sub + all[j].id);
            if(temp == input[i].name){
                addedCourses.push({course : all[j], semester : SemToNum(input[i].semester)})
            }
        }
    }

}


function SortAllCourseBySemester(){
    for(i=0; i<16; i++)
        schedule.push([])
    for(i=0; i<addedCourses.length; i++){
        schedule[addedCourses[i].semester].push(addedCourses[i].course)
    }
}


function CheckThisCourse(course, sem){
    var timecheck = true
    switch(sem%4){
        case 0 :
            if(course.semester.summer!="y")
                timecheck = false;
            break
        case 1 :
            if(course.semester.fall!="y")
                timecheck = false;
            break
        case 2 :
            if(course.semester.winter!="y")
                timecheck = false;
            break
        case 3 :
            if(course.semester.spring!="y")
                timecheck = false;
            break
    }
    if(!timecheck){
        error.push({name:(course.sub + course.id), semester : NumToSem(sem), message : "course not offer in this qurater"})
        return
    }
    for(i=0; i<course.prereq.length; i++){
        var range = sem-1
        var found = false
        if(course.prereq[i].concur=="y")
            range+=1
        for(j=0; j<=range; j++){
            for(k=0; k<schedule[j].length; k++){
                if(course.prereq[i].sub == schedule[j][k].sub &&
                    course.prereq[i].id == schedule[j][k].id){
                    found = true;
                    break
                }
            }
            if(found) break
        }
        if(!found) error.push({name:(course.sub + course.id), semester : NumToSem(sem), message : "course's prerequisites are not fulfilled"})

    }
}

CheckThisCourse(course1,1)

function Validation(input, all){
    addedCourses(input,all)
    SortAllCourseBySemester()
    for(i=0; i<16; i++){
        for(j=0; j<schedule[i].length; j++){
            CheckThisCourse(schedule[i][j],schedule[i])
        }
    }

}

Validation(inputCourses,allCourses)








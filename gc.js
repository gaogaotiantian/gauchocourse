var course1 = {
    label : "CMPSC 8 Introduction to Computer Science",
    sub: "CMPSC",
    id : "8",
    prereq : [{type : "precourse", precourse: {sub : "MATH", id : "3A", concur : "y"}}],
    units :4,
    semester : {"spring":"y", "summer":"y", "fall":"y", "winter":"y"}
}

var course2 = {
    label :"CMPSC 16 Problem Solving with Computers I",
    sub : "CMPSC",
    id : "16",
    units : 4,
    prereq : [{type: "precourses", precourses : [{sub : "MATH",  id : "3A",  concur : "y"}, {sub : "MATH",  id : "34A",  concur : "y"}]},
            {type: "precourse", precourse : {sub : "CMPSC", id :"8", concur :"n"}}],
    semester : {"spring":"y", "summer":"y", "fall":"y", "winter":"y"}

}

var course3 = {
    label :"Math 3A, Introduction to Calclus",
    sub : "MATH",
    id : "3A",
    units : 4,
    prereq : [],
    semester : {"spring":"y", "summer":"y", "fall":"y", "winter":"y"}

}

var course4 = {
    label :"Math 34A, Introduction to Calclus",
    sub : "MATH",
    id : "34A",
    units : 4,
    prereq : [],
    semester : {"spring":"y", "summer":"y", "fall":"y", "winter":"y"}

}



var inputCourses = [
                    {name : "CMPSC8", semester : "freshmenFall"},
                    {name : "CMPSC16", semester : "freshmenWinter"},
                    {name : "MATH3A", semester : "freshmenSummer"},
                    {name : "MATH34A", semester : "freshmenSummer"}
] //input courses name with semester that should be provied for the function, this is just a example

var allCourses  = [course1,course2,course3,course4] //list of all courses as pbject

var addedCourses = [] //list of all inputed courses as a object of course and semester

var schedule = [] //sorted schedule, index represent the semester. ex: schedule[0] is the array of all input courses in freshmen summer quarter

var error = [] // array of error as object, each object has three variable. 1.name 2.semester 3.message

var check = "" //only for debug purpose

var totalUnit = 0 // totoal units of the current courses add up

var quarterUnit = [] // unit for each quarter, ex: quarterUnit[0] represent the unit of the freshmen summer quarter

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
  
//add all the input courses to the addedcourse
function AddAllCourses(input, all){
    for(i=0; i<input.length; i++){
        for(j=0; j<all.length; j++){
            var temp = (all[j].sub + all[j].id);
            if(temp == input[i].name){
                addedCourses.push({course : all[j], semester : SemToNum(input[i].semester)})
            }
        }
    }

}

//add the courses from addedcourses into schedule in the semester order
function SortAllCourseBySemester(){
    for(i=0; i<16; i++)
        schedule.push([])
    for(i=0; i<addedCourses.length; i++){
        schedule[addedCourses[i].semester].push(addedCourses[i].course)
    }
}


//function to check if taking certian course in certain semester is allowed
function CheckThisCourse(course, sem){
    var timecheck = true
    var prelength = course.prereq.length
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
        error.push({name:(course.sub + course.id), semester : NumToSem(sem), message : "course not offer in this quarter"})
        return
    }
    
    
    for(n in course.prereq){
        if(course.prereq[n].type == "precourse"){
            var range = sem-1
            var found = false
            if(course.prereq[n].precourse.concur == "y")
                range+=1
            for(s=0; s<=range; s++){
                for(q in schedule[s]){
                    if(course.prereq[n].precourse.sub == schedule[s][q].sub&&
                        course.prereq[n].precourse.id == schedule[s][q].id){
                        found = true
                        break
                    }
                }
                if(found) break
            }
            if(!found){
                error.push({name:(course.sub + course.id), semester : NumToSem(sem), message : "course's prerequisites are not fulfilled"})
                return
            }
        }

        else if(course.prereq[n].type == "precourses"){
            var found = false
            for(p in course.prereq[n].precourses){
                var range = sem-1
                var sub = course.prereq[n].precourses[p].sub
                var id = course.prereq[n].precourses[p].id
                if(course.prereq[n].precourses[p].concur == "y")
                    range+=1
                for(s=0; s<=range; s++){
                    for(q in schedule[s]){
                        if(sub == schedule[s][q].sub&&
                            id == schedule[s][q].id){
                            found = true
                            break
                        }
                    }
                if(found) break
                }
                if(found) break
            }
            if(!found){
                error.push({name:(course.sub + course.id), semester : NumToSem(sem), message : "course's prerequisites are not fulfilled"})
                return
            }
        }
    }
    
}

function CountUnit(){
    var tempunit = 0
    for(a =0; a<schedule.length; a++){
        for(b in schedule[a]){
            tempunit+=schedule[a][b].units
        }
        quarterUnit.push(tempunit)
        totalUnit+=tempunit
        tempunit = 0
    }
}

//main function that caller should provide the argument to run the validation
function Validation(input, all){
    AddAllCourses(input,all)
    SortAllCourseBySemester()
    for(i=0; i<16; i++){
        for(j=0; j<schedule[i].length; j++){
            CheckThisCourse(schedule[i][j],i)
        }
    }
    CountUnit()

}

Validation(inputCourses,allCourses)


function change(){
    var x = document.getElementById('demo');
    x.innerHTML = quarterUnit[0] 
}

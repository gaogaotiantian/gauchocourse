var addedCourses = [] //list of all inputed courses as a object of course and semester

var schedule = [] //sorted schedule, index represent the semester. ex: schedule[0] is the array of all input courses in freshman summer quarter

var totalUnit = 0 // totoal units of the current courses add up

var quarterUnit = [] // unit for each quarter, ex: quarterUnit[0] represent the unit of the freshman summer quarter


//main function that caller should provide the argument to run the validation
function ValidateAllInput(input){
    addedCourses = []
    schedule = []
    invalidData = [] 
    validCourses = []
    AddAllCourses(input)
    SortAllCourseBySemester()
    for(var i=0; i<16; i++){
        for(var course of schedule[i]){
            CheckThisCourse(course,i)
        }
    }
    CountUnit()
    console.log("added:", addedCourses)
    console.log("valid:", validCourses)
    console.log("invalid", invalidData)
}


function IsValid(name){
    if(name == "") return true
    for(course of validCourses){
        if(name == course.label)
            return true
    }
    return false
}

function GetErrorMessage(name){
    if(name == "") return true
    console.log("invalid", invalidData)
    for(er of invalidData){
        if(er.name ==name)
            return er.message
    }
    return ""
}







function SemToNum(semester){
    if(semester == "freshman_summer") return 0;
    if(semester == "freshman_fall") return 1;
    if(semester == "freshman_winter") return 2;
    if(semester == "freshman_spring") return 3;
    if(semester == "sophomore_summer") return 4;
    if(semester == "sophomore_fall") return 5;
    if(semester == "sophomore_winter") return 6;
    if(semester == "sophomore_spring") return 7;
    if(semester == "junior_summer") return 8;
    if(semester == "junior_fall") return 9;
    if(semester == "junior_winter") return 10;
    if(semester == "junior_spring") return 11;
    if(semester == "senior_summer") return 12;
    if(semester == "senior_fall") return 13;
    if(semester == "senior_winter") return 14;
    if(semester == "senior_spring") return 15;
}

function NumToSem(num){
        if(num==0) return "freshman_summer";
        if(num==1) return "freshman_fall";
        if(num==2) return "freshman_winter";
        if(num==3) return "freshman_spring";
        if(num==4) return "sophomore_summer";
        if(num==5) return "sophomore_fall";
        if(num==6) return "sophomore_winter";
        if(num==7) return "sophomore_spring";
        if(num==8) return "junior_summer";
        if(num==9) return "junior_fall";
        if(num==10) return "junior_winter";
        if(num==11) return "junior_spring";
        if(num==12) return "senior_summer";
        if(num==13) return "senior_fall";
        if(num==14) return "senior_winter";
        if(num==15) return "senior_spring";
    }
  
//add all the input courses to the addedCourses
function AddAllCourses(input){
    var existence = false
    var tempname
    for(i=0; i<input.length; i++){
        for(j=0; j<courseData.length; j++){
            var temp = (courseData[j].label);
            if(temp == input[i].course){
                for(z in addedCourses){
                    tempname = (addedCourses[z].course.label)
                    if(tempname == input[i].name){
                        existence = true
                        break
                    }
                }
                if(existence){
                    existence = false
                    break
                }
                addedCourses.push({course : courseData[j], semester : SemToNum(input[i].semester)})
            }
        }
    }

}

//add the courses from addedCourses into schedule in the semester order
function SortAllCourseBySemester(){
    for(i=0; i<16; i++)
        schedule.push([])
    for(i=0; i<addedCourses.length; i++){
        schedule[addedCourses[i].semester].push(addedCourses[i].course)
    }
}

//giving a course name, it will return the course object corresponing to this name
function GetCourseByName(name){
    var tpname
    for(var course of courseData){
        tpname = (course.label)
        if(tpname == name)
            return course
    }
}




//function to check if taking certian course in certain semester is allowed
function CheckThisCourse(course, sem){
    for(var c of validCourses){
        if(c.label == course.label)
            return
    }

    console.log(course)
    var timecheck = true
    switch(sem%4){
        case 0 :
            if(course.semester.indexOf("summer")<0)
                timecheck = false;
            break
        case 1 :
            if(course.semester.indexOf("fall")<0)
                timecheck = false;
            break
        case 2 :
            if(course.semester.indexOf("winter")<0)
                timecheck = false;
            break
        case 3 :
            if(course.semester.indexOf("spring")<0)
                timecheck = false;
            break
    }
    if(!timecheck){
        invalidData.push({name:(course.label), semester : NumToSem(sem), message : "course not offer in this quarter"})
        console.log("prereq" + invalidData)
        return
    }
    
    
    for(n in course.prereq){
            var found = false
            for(var p in course.prereq[n]){
                var range = sem-1
                var id = course.prereq[n][p].id
                if(course.prereq[n][p].concur == "y")
                    range+=1
                    for(var s=0; s<=range; s++){
                        for(var q in schedule[s]){
                            if(id == schedule[s][q].id){
                                var tempcourse = courseData[id]
                                CheckThisCourse(tempcourse,s)
                                for(var h of validCourses){
                                    if(h.label == tempcourse.label){
                                        found = true
                                        break
                                    }
                                }
                            }
                            if(found) break
                        }
                    if(found) break
                    }
                                
                if(found) break
            }
            if(!found){
                invalidData.push({name:(course.label), semester : NumToSem(sem), message : "course's prerequisites are not fulfilled"})
                console.log("prereq" + invalidData)
                return
            }
        
    }
    validCourses.push(course)
}

function CountUnit(){
    var tempunit = 0
    for(qt of schedule){
        for(course of qt){
            tempunit+=Math.round(course.units)
        }
        quarterUnit.push(tempunit)
        totalUnit+=tempunit
        tempunit = 0
    }
}

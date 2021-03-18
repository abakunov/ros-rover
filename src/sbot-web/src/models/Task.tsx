import { TaskStatus } from "../enums/taskStatus";

export class Task{
    name:string;
    status: TaskStatus;
    propName:string;
    propValue:string;

    fromObj(obj : any):void{
        this.name = obj.name;
        this.status = TaskStatus.waiting;
        this.propName = obj.propName;
        this.propValue = obj.propValue;
    }

    constructor(name:string,status:TaskStatus, propName:string, propValue:string) {
        this.name = name;
        this.status = status;
        this.propName = propName;
        this.propValue = propValue;
    }


}

function TaskfromObj(obj:any):Task{
    let tsk : Task = new Task(
        "",
        TaskStatus.waiting,
        "",
        ""
    );
    tsk.name = obj.name;
    tsk.status = TaskStatus.waiting;
    tsk.propName = obj.propName;
    tsk.propValue = obj.propValue;
    
    return tsk;
}

function TaskfromJson(json:string):Task{
    const obj = JSON.parse(json);
    return TaskfromObj(obj);
}


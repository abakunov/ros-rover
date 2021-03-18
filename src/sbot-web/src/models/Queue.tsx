import { TaskStatus } from "../enums/taskStatus";
import { Task } from "./Task";

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

export class Queue{

    data: Array<Task>;

    fromJson(json : string): void{
        
        
        const obj = JSON.parse(json);
        var tasks = obj.tasks;
        this.data = [];
        tasks.forEach((task:any) => {
            this.data.push(TaskfromObj(task));
        });
    }

    constructor(data : Array<Task>){
        this.data = data;
    }

}
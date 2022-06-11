import config from "@/config";
import { v4 as uuidv4 } from "uuid";

///



///

export async function getMedicines() {   
    const endPoint = `${config.API_PATH}/medicines`
    const settings = {method: "GET"};
    
    const response = await fetch(endPoint,settings);
    return await response.json();
}

export async function getMedicineById(id) {   
    const endPoint = `${config.API_PATH}/medicines/${id}`
    const settings = {method: "GET"};

    const response = await fetch(endPoint,settings);
    return await response.json();
}

export async function getListMedicinesByDate(){
    let date = new Date();
    let today = date.toISOString().split("T")[0];
    let endpoint = `${config.API_PATH}/medicines/by-date/${today}`;
    const settings = {method: "GET"};

    
    const response = await fetch(endpoint, settings);
    return await response.json();
}

export async function saveMedicine(medicine){
    const addMedicine = medicine
    addMedicine.id_medicine = uuidv4();

    const endPoint = `${config.API_PATH}/medicines`; 
    const settings = {
        method: "POST",
        body: JSON.stringify(addMedicine),
        headers: {
            "Content-Type": "application/json",
        },
      };
    await fetch(endPoint, settings);
    
}



export async function deleteMedicine(id) {
    const endPoint = `${config.API_PATH}/medicines/${id}`
    const settings = {method: "DELETE"};

    const response = await fetch(endPoint, settings);
    return response;
}


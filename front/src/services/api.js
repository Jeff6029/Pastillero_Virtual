import config from "@/config";
// import { v4 as uuidv4 } from "uuid";

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
  
export async function deleteMedicine(id) {
    const endPoint = `${config.API_PATH}/medicines/${id}`
    const settings = {method: "DELETE"};

    const response = await fetch(endPoint, settings);
    return response;
}
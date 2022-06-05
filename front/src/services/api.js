import config from "@/config";
// import { v4 as uuidv4 } from "uuid";

///



///

export async function getMedicine(id) {   
    const endPoint = `${config.API_PATH}/medicines/${id}`
    
    const response = await fetch(endPoint);
    return await response.json();
}
  
export async function deleteMedicine(id) {
    const endPoint = `${config.API_PATH}/medicines/${id}`
    const settings = {method: "DELETE"};

    const response = await fetch(endPoint, settings);
    return await response.json();
}
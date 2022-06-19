import config from "@/config";
import { v4 as uuidv4 } from "uuid";

/// USERS

function getUserId() {
    const userJson = localStorage.getItem("auth");
    const user = JSON.parse(userJson);
    return user.id_user;
  }

// function getAccessToken() {
//     const jwtJson = localStorage.getItem("auth");
//     const jwt = JSON.parse(jwtJson);
//     return jwt.access_token;
//   }


/// HTTP

export async function getMedicines() {   
    const endPoint = `${config.API_PATH}/medicines`
    const settings = {
        method: "GET",
        headers: {
            Authorization: getUserId(),
        }
    };
    
    const response = await fetch(endPoint,settings);
    return await response.json();
}

export async function getMedicineById(id) {   
    const endPoint = `${config.API_PATH}/medicines/${id}`
    const settings = {
        method: "GET",
        headers: {
            Authorization: getUserId()
        }
    };

    const response = await fetch(endPoint,settings);
    return await response.json();
}

export async function getListMedicinesByDate(){
    let date = new Date();
    let today = date.toISOString().split("T")[0];

    let endpoint = `${config.API_PATH}/medicines/by-date/${today}`;
    const settings = {
        method: "GET",
        headers: {
            Authorization: getUserId(),
        }
    };
    
    const response = await fetch(endpoint, settings);
    return await response.json();
}

export async function deleteMedicine(id) {
    const endPoint = `${config.API_PATH}/medicines/${id}`
    const settings = {
        method: "DELETE",
        Authorization: getUserId()};

    const response = await fetch(endPoint, settings);
    return response;
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
            Authorization: getUserId(),
        },
      };

    await fetch(endPoint, settings);
    
}

export async function updateMedicine(medicine){
    const endPoint = `${config.API_PATH}/medicines/${medicine.id_medicine}`
    const settings = {
        method: "PUT",
        body: JSON.stringify(medicine),
        headers: {
          "Content-Type": "application/json",
          Authorization: getUserId(),
        },
      };
      await fetch(endPoint, settings);
}
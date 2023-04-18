import React, { useEffect, useState } from 'react';
import List from "../Page/Dashboard/List.js";
// import Home from "./pages/Home";

const Home = (props) => {

let p;
    if(props.name) {
        // console.log(props.name)
        p=(
            
            <List/>
        )
    }
    else { 
        // console.log(props.name)
        p=(
            
            'Currently You are not Logged In'
        )
    }
    return (
       
        <div>
            
           {p}
           {/* {props.name ? <List/> : "Currently You are not Logged In"} */}
        </div>
        
        
       
    );
};

export default Home;
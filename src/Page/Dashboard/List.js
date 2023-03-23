import React from 'react'
import './table.css'


class List extends React.Component{

    constructor(){
        super();
        this.state={
            data:[], data2:[]
        };
    }

    fetchData(){
        fetch('http://127.0.0.1:8000/notesheet/')
        .then(response=>response.json())
        .then((data)=>{
            this.setState({
                data:data
            });
            console.log(data)
        });
        fetch('http://127.0.0.1:8000/faculty/')
        .then(response=>response.json())
        .then((data2)=>{
            this.setState({
                data2:data2
            });
            console.log(data2)
        });
    }

 

    componentDidMount(){
        this.fetchData();
    }

    // constructor(){
    //     super();
    //     this.state={
    //         data2:[]
    //     };
    // }



   
    render(){

        const noteSheet=this.state.data;
        const noteSheet2=this.state.data2;
        const rows2=noteSheet2.map((note)=>
            <td>{note.Name}</td>
          
        );

        const rows=noteSheet.map((note,i)=>
        <tr key={note.f_id}>
        <td>{note.id}</td>
        <td>{note.subject}</td>  
        <td>{rows2[i]}</td>   
      <td>  {note.date}</td>




        <td className='text-right'>
            <button className='button muted-button'>Approve</button>
        </td>
        <td className='text-center'>
            <button className='button muted-button'>Reject</button>
        </td>
        <td className='text-center'>
            <button className='button muted-button'>Review</button>
        </td>
        <td className='text-left'>
            <button className='button muted-button'>Forward</button>
        </td>
    </tr>
            // <tr key={emp.id}>
            //     <td>{emp.full_name}</td>
            //     <td>{emp.email}</td>
            //     <td>{emp.contact}</td>
            //     <td>{emp.address}</td>
            //     <td>
            //         <Link to={'update/'+emp.id} className="btn btn-info mr-2">Update</Link>
            //         <button onClick={()=>this.deleteData(emp.id)} className="btn btn-danger">Delete</button>
            //     </td>
            // </tr>
        );
        
        return (
            <div className='contain-table'>
                <table className='table'>
                    <thead>
                        <tr>
                        <th>No.</th>
                        <th>Notesheet</th>
                        <th>Sender's name</th>
                        <th>Date</th>
                        <th colSpan={2} className='text-center'>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                      {rows}
                    </tbody>
                </table>
            </div>
        );
    }
  
    
}


// function List({ faculty }){
//     return (
//     <div className='contain-table'>
//         <table className='striped-table'>
//             <thead>
//                 <tr>
//                 <th>No.</th>
//                 <th>Notesheet</th>
//                 <th>Sender's name</th>
//                 <th>Date</th>
//                 <th colSpan={2} className='text-center'>Actions</th>
//                 </tr>
//             </thead>
//             <tbody>
//                 {faculty.length > 0 ? (
//                     faculty.map((faculty, i) => (
//                         <tr key={faculty.id}>
//                             <td>{i + 1}</td>
//                             <td>{faculty.name}</td>
//                             <td>{faculty.sender}</td>
//                             <td>{faculty.date}</td>
//                             <td className='text-right'>
//                                 <button className='button muted-button'>Approve</button>
//                             </td>
//                             <td className='text-center'>
//                                 <button className='button muted-button'>Reject</button>
//                             </td>
//                             <td className='text-center'>
//                                 <button className='button muted-button'>Review</button>
//                             </td>
//                             <td className='text-left'>
//                                 <button className='button muted-button'>Forward</button>
//                             </td>
//                         </tr>
//                     ))
//                 ) : (
//                     <tr>
//                         <td colSpan={5} > No faculty</td>
//                     </tr>
//                 )}
//             </tbody>
//         </table>
//     </div>
//     )
// }

export default List
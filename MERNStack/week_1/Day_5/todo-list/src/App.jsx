import './App.css';
import {useState } from 'react'
import Formm from './components/Formm';
import Todolistt from './components/Todolistt';
function App() {
  const tasks=[{title:"Get Python black belt.",check:false},
  ]
  const [list,setList]=useState(tasks)
  const updatePosts = (newPost) =>{
    console.log("updated");
    setList([...list,newPost])
  }
  // delete a post
  const deletePost = (postId) => {
    console.log("before", list);
    const updatedPosts = list.filter((onePost, idx) => {
      return idx !== postId;
    });
    console.log("after", updatedPosts);
    setList(updatedPosts);
  };

// read a post
const readPost = (postId) => {
  const copyList = [...list];
  copyList[postId].check = !copyList[postId].check;
  setList(copyList);
};

  return (
    <div className="App">
      <Formm updatePosts={updatePosts} />
      <Todolistt list={list} deletePost={deletePost} readPost={readPost} />
    </div>
  );
}
export default App;
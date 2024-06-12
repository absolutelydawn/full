import React from 'react';


function App() {
    const users = [
        {id:1, username: 'developer', email: 'public.developer@gmail.com'},
        {id:2, username: 'tester', email: 'public.tester@gmail.com'},
        {id:3, username: 'dawn', email: 'public.dawn@gmail.com'},
    ];

    const nestId = useRef(4);
    const onCreate = () => {
        nextId.current += 1;
    };
  return <UserList users={users} />;
}

export default App;
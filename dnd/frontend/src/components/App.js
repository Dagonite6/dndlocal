import React, { Component } from "react";
import { render } from "react-dom";
import { Button } from 'react-bootstrap';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }

  componentDidMount() {
    fetch("api/character")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          };
        });
      });
  }

  render() {
    return (
      <div className="container p-3 my-3 bg-dark text-white">
      <h1>React fetch from Django REST api with PostgresDB</h1>   
      <ul>
        {this.state.data.map(contact => {
          return (
            <li key={contact.id}>
              <p>Name: {contact.name}</p>
              <p>Title: {contact.title}</p>
              <p>Level: {contact.level}</p>
              <p>Race: {contact.race}</p>
              <p>Class: {contact.type}</p>
              <p>History: {contact.history}</p>
            </li>
          );
        })}
      </ul>
      <Button variant="primary">Primary</Button>{' '}
      </div>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
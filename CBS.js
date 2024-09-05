import React, { Component } from 'react'

export default class CBS extends Component {
  render() {
    return (
      <div>
        <p>Welcome CBC{this.props.value}</p>
      </div>
    )
  }
}

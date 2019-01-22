import React, {Component} from 'react'
import {Button, Form, Container} from 'semantic-ui-react'
import axios from 'axios'
import {Redirect} from 'react-router-dom'
import {connect} from 'react-redux'
import {gettingUserData} from '../reducer'

class InputForm extends Component{
  constructor() {
    super()
    this.state = {
      username: '',
      redirect: false
    }
    this.onChange = this.onChange.bind(this)
    this.onSubmit = this.onSubmit.bind(this)
  }

  async onSubmit(e) {
    console.log('in form submit')
    this.props.gettingUserData(this.state.username);
    // let response = await axios.get(`/${this.state.username}`, this.state.username);
    // console.log(response);
    // console.log(typeof response.data);
    // console.log(response.data.avatar);
    this.setState({redirect: true})
    //put username and response.data on the store and re-direct to Analysis results. there,
  }

  onChange(e) {
    this.setState({username: e.target.value})
  }

  render() {
    return (
      <Container>
        {
          this.state.redirect ? (
            <Redirect to="/analysis" />
          ) : (
            <Form onSubmit={this.onSubmit}>
              <Form.Field>
                <label>username</label>
                <Form.Input placeholder=' careful of spelling!' onChange={this.onChange} value={this.state.username} />
              </Form.Field>
              <Form.Button type="submit" >Submit</Form.Button>
            </Form>
          )
        }

      </Container>
    )
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    gettingUserData: (user) => dispatch(gettingUserData(user))
  }
}

export default connect(null, mapDispatchToProps)(InputForm)

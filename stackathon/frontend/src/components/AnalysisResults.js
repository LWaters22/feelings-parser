import {Container, Grid, Header, Image, Button} from 'semantic-ui-react'
import React, {Component} from 'react'
import axios from 'axios'
import {connect} from 'react-redux'

class AnalysisResults extends Component {
  constructor(props) {
    super()
    this.state = {
      analysis: ''
    }
  }

  async componentDidMount() {
    console.log('in component did mount')
    if (!this.props.username) {
      console.log('still waiting')
    } else {
      const {data} = await axios.get(`analysis/${this.props.username}`)
      console.log(data);
    }
    //axios get analysis info by using the username on store
  }

  async componentDidUpdate() {
    console.log('in component did mount')
    if (!this.props.username) {
    } else {
      const { data } = await axios.get(`analysis/${this.props.username}`)
      this.setState({analysis: data.analysis})
    }
  }

  render() {
    return (
      <Container>
        {
          this.props.fullname ? (
        <Grid centered>
          <Grid.Row>
            <Header>Here is how {this.props.fullname} has been tweeting</Header>
          </Grid.Row>
          <Grid.Row>
            <Image src={this.props.avatar} />
          </Grid.Row>
          <Grid.Row>
            {
              this.state.analysis ? (
                <Header>{this.state.analysis}</Header>
                // <Button onSubmit=>Try again?</Button>
              ) : (
                <Header>Loading</Header>
              )
            }
          </Grid.Row>
        </Grid>
          ) : (
            <Header>Loading</Header>
          )
        }
      </Container>
    )
  }
}

const mapStateToProps = (state) => {
  return {
    fullname: state.fullname,
    username: state.username,
    avatar: state.avatar
  }
}

const mapDispatchToProps = (dispatch) => {
  return {

  }
}

export default connect(mapStateToProps, mapDispatchToProps)(AnalysisResults)

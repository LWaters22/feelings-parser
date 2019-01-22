import {Container, Grid, Header, Image} from 'semantic-ui-react'
import React, {Component} from 'react'
import axios from 'axios'
import {connect} from 'react-redux'

class AnalysisResults extends Component {
  constructor(props) {
    super()
    this.state = {

    }
  }

  componentDidMount() {
    //axios get analysis info by using the username on store
  }

  render() {
    return (
      <Container>
        <Grid centered>
          <Grid.Row>
            <Header>Here is how {this.props.fullname} has been tweeting</Header>
          </Grid.Row>
          <Grid.Row>
            <Image src={this.props.avatar} />
          </Grid.Row>
        </Grid>
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

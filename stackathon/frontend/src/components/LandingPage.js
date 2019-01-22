import React from 'react'
import { Header, Container, Grid } from 'semantic-ui-react'
import InputForm from './InputForm'

const LandingPage = () => {
  return (
    <Container>
      <Grid centered>
        <Grid.Row>
          <Header>Whose tweets would you like to look at?</Header>
        </Grid.Row>
        <Grid.Row>
          <InputForm />
        </Grid.Row>
      </Grid>
    </Container>
  )
}

export default LandingPage

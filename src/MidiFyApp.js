import React from 'react';
import { Layout, Menu, Card, Avatar, Row, Col } from 'antd';

const { Header } = Layout;

function MidiFyApp() {
  return (
    <Layout>
      <Header>
        <div className="logo" />
        <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['2']}>
          <Menu.Item key="1">nav 1</Menu.Item>
          <Menu.Item key="2">nav 2</Menu.Item>
          <Menu.Item key="3">nav 3</Menu.Item>
        </Menu>
      </Header>
      <Row gutter={16}>
        <Col span={8}>
          <Card
            cover={
              <img
                alt="example"
                src="https://via.placeholder.com/140x140"
              />
            }
          >
            <Card.Meta
              avatar={<Avatar src="https://via.placeholder.com/80x80" />}
              title="Song Title"
              description="Author: John Doe"
            />
            <div className="card-info">
              <p>Date: 01/01/2023</p>
              <p>Cost: 1 ETH</p>
              <p>Plays: 100</p>
            </div>
          </Card>
        </Col>
      </Row>
    </Layout>
  );
}

export default MidiFyApp;

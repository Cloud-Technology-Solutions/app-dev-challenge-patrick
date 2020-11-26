package com.qlouder;

import com.google.api.server.spi.config.Api;
import com.google.api.server.spi.config.ApiMethod;

@Api(name = "api", version = "v1")
public class Endpoint {

    @ApiMethod(name = "helloWorld", httpMethod="GET")
    public HelloWorldResponse helloWorld() {
        HelloWorldResponse hello = new HelloWorldResponse();
        hello.response = "Hello World!";
        return hello;
    }
}

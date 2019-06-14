FROM rust:latest

ENV USER=Shane

RUN cargo new myapp --bin
 
COPY /src/ /myapp/src/
COPY Cargo.toml /myapp/Cargo.toml
WORKDIR /myapp/

CMD ["cargo", "run"]
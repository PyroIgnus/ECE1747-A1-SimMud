#include <iostream>

#include "Log.h"

TSLogger* TSLogger::instance = NULL;

TSLogger::TSLogger(){
    this->mutex = SDL_CreateSemaphore(1);
}

TSLogger::~TSLogger(){
    SDL_DestroySemaphore(this->mutex);
    this->close();
}

void TSLogger::initialize(){
    TSLogger::instance = new TSLogger();
}

TSLogger* TSLogger::getInstance(){
    return TSLogger::instance;
}

void TSLogger::open(std::string filename){
    this->outfile.open(filename.c_str(), std::fstream::in | std::fstream::out | std::fstream::trunc | std::ios::binary);
}

void TSLogger::close(){
    this->outfile.close();
}

bool TSLogger::write(uint32_t thread_id, uint32_t tick_count,
    uint32_t request_count, uint32_t request_time, uint32_t update_count, uint32_t update_time){
    if(!this->outfile.is_open()){
        return false;
    }

    SDL_SemWait(this->mutex);
    this->outfile << thread_id     << ", ";
    this->outfile << tick_count    << ", ";
    this->outfile << request_count << ", ";
    this->outfile << request_time  << ", ";
    this->outfile << update_count  << ", ";
    this->outfile << update_time   << std::endl;
    SDL_SemPost(this->mutex);
    return true;
}

"""Jobs for nautobot_docker_compose."""
from nautobot.extras.jobs import register_jobs
from .hello_world import HelloWorldJob

register_jobs(HelloWorldJob)

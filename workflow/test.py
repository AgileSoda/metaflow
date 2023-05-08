from metaflow import Flow, namespace
namespace(None)
for name in ['Workflow1', 'Workflow2', 'Workflow2_mod1']:
    run = Flow(name).latest_run
    print(run.successful)
    
    
flow_name = 'Workflow1'
flow = Flow(flow_name)
latest_run = flow.latest_run

from metaflow import Run
directly_accessed_run = Run('{}/{}'.format(
    flow_name, latest_run.id))

run = Flow(name).latest_run
steps = list(run.steps())[::-1]
for task in steps[-1].tasks():
    print(task)
import hudson.model.*

def viewName = "TESTView"
def search = "-Dev"
def replace = "-RELEASE"

def view = Hudson.instance.getView(viewName)

/* now you copy all jobs of the view copy all projects of a view */
for(item in view.getItems()) {

  /* create the new project name */
  newName = item.getName().replace(search , replace)

  /* now copy the job */
  def job = Hudson.instance.copy(item, newName)
  job.save()

}
